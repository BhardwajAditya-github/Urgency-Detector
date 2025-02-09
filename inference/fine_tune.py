import torch
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset
from peft import LoraConfig, get_peft_model, TaskType

df = pd.read_csv("urgency_data.csv")

def preprocess_data(examples):
    return {
        "text": [f"Classify this conversation: {conv}" for conv in examples["conversation"]],
        "label": examples["label"]
    }

dataset = Dataset.from_pandas(df).map(preprocess_data)

# Load tokenizer and model
MODEL_NAME = "deepseek-ai/deepseek-llm-7b"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

dataset = dataset.map(tokenize_function, batched=True)

label_map = {label: i for i, label in enumerate(df["label"].unique())}
dataset = dataset.map(lambda x: {"labels": label_map[x["label"]]})

peft_config = LoraConfig(task_type=TaskType.SEQ_CLS, r=8, lora_alpha=32, lora_dropout=0.1)
model = get_peft_model(model, peft_config)

training_args = TrainingArguments(
    output_dir="./deepseek-finetuned",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    save_steps=500,
    save_total_limit=2,
    evaluation_strategy="epoch",
    logging_dir="./logs",
    report_to="none",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    tokenizer=tokenizer,
)

trainer.train()

trainer.save_model("./deepseek-finetuned")
tokenizer.save_pretrained("./deepseek-finetuned")

print("Fine-tuning complete! Model saved.")
