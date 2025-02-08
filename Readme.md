# Urgency Detector

## Project Overview
The Urgency Detector is a machine learning model designed to detect scam calls by identifying different types of urgency created by scammers in a textual conversation between a scammer and a normal person. The model is built on top of the DeepSeek model and aims to categorize the urgency into various meaningful classes.

## Features
- Detects different types of urgency in a conversation
- Classifies urgency into multiple categories such as:
  - No Urgency
  - Emotional Urgency
  - Family Urgency
  - Financial Urgency
  - Medical Urgency
  - Legal Urgency
  - Social Urgency
  - Time-sensitive Urgency

## Requirements
- Python 3.x
- DeepSeek model
- Required libraries (to be added as per the implementation)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/urgency-detector.git
    ```
2. Navigate to the project directory:
    ```bash
    cd urgency-detector
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Prepare the dataset: Provide textual conversations between a scammer and a normal person.
2. Train the model:
    ```bash
    python train.py --data_path path/to/dataset
    ```
3. Evaluate the model:
    ```bash
    python evaluate.py --model_path path/to/trained_model --data_path path/to/test_data
    ```
4. Detect urgency in a new conversation:
    ```bash
    python detect.py --model_path path/to/trained_model --input_text "Your input conversation here"
    ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or inquiries, please contact [Your Name](mailto:your.email@example.com).

---

Feel free to customize the `README.md` file further according to your specific requirements. If you need any more assistance, just let me know!
