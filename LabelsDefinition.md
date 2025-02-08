# Urgency Detector Dataset - Labels and Definitions

The **Urgency Detector** is a machine learning model designed to detect scam calls by identifying different types of urgency in textual conversations between a scammer and a victim. Below are the defined labels for the dataset, each describing a unique type of urgency that scammers use to manipulate their targets.

---

## Labels and Definitions

### 1. **Emotional Urgency**
   - **Definition**: Scammers use **emotionally charged situations** to manipulate the victim. This type of urgency is based on preying on personal relationships and emotions such as **guilt**, **sympathy**, **fear**, or **love**. The victim is made to feel emotionally responsible for the situation at hand, often related to loved ones or pets.
   - **Key Focus**: Emotional manipulation, relationship-based distress, feelings of responsibility and connection.
   - **Example**: A scammer might claim that a family member is in critical danger or that a pet is lost, urging the victim to act quickly because they feel an emotional attachment.
   - **Edge Cases**: TO handle scenarios such as acutal son calls and asks his mom for help, we need to ensure the model considers context and relationship in the conversations. For example, the tone, nature of the conversation, and relationship between the caller and receiver should be factored in. We must include actual conversation of this type under "No Urgency" label.
---

### 2. **Financial Urgency**
   - **Definition**: The scammer creates **financial pressure**, making the victim feel as though they are about to lose money, assets, or financial security unless they act immediately. This urgency typically involves fraud, payments, or financial penalties.
   - **Key Focus**: Money, assets, accounts, financial distress.
   - **Example**: A scammer might claim that there’s fraud on the victim’s account, or that they need to pay an urgent fee to avoid a financial penalty or loss of funds.

---

### 3. **Legal/Authority Urgency**
   - **Definition**: The scammer uses **fear of legal or authoritative consequences** to manipulate the victim. This urgency involves threats of **arrest**, **prosecution**, **legal action**, or **severe penalties** if the victim does not comply immediately. Scammers pretend to be from law enforcement, government agencies, or legal firms to create pressure.
   - **Key Focus**: Legal threats, authorities, police, fines, jail time, etc.
   - **Example**: A scammer might claim to be a government agent, stating that the victim owes money or has committed an illegal act and must pay immediately to avoid arrest or jail time.

---

### 4. **Health/Medical Urgency**
   - **Definition**: Scammers exploit the victim’s **concern for health** and **medical emergencies**. They fabricate health-related crises, such as a loved one being in critical condition or needing urgent medical procedures that require immediate funds. This form of urgency often triggers fear and empathy.
   - **Key Focus**: Medical conditions, health-related emergencies, hospitals, doctors, treatments.
   - **Example**: A scammer could tell the victim that their relative is in a life-threatening condition and needs immediate treatment that must be paid for upfront to save their life.

---

### 5. **Romantic Urgency**
   - **Definition**: Scammers manipulate the victim’s **romantic feelings** or **personal relationships** to create urgency. This type of scam may involve claiming that a partner, spouse, or love interest is in a critical situation and needs immediate help. The victim may feel pressured to act quickly out of **love**, **responsibility**, or a desire to help.
   - **Key Focus**: Romantic relationships, emotional bonds, feelings of love or attachment.
   - **Example**: A scammer might pretend to be the victim’s partner, claiming they are in danger or need urgent help, pushing the victim to act based on romantic obligation or emotional manipulation.

---

### 6. **Social/Peer Pressure Urgency**
   - **Definition**: Scammers use **social influence** or **peer pressure** to manipulate the victim. The victim is made to feel that they need to act quickly to avoid social embarrassment, exclusion, or judgment. This can be framed as a **group emergency** or something that requires the victim to be seen as helpful, responsible, or supportive by others.
   - **Key Focus**: Social status, reputation, peer influence, group dynamics.
   - **Example**: A scammer might claim that the victim’s friends or family are relying on them for help, or that they will face social consequences if they do not act quickly.

---

## Conclusion

Each of these labels represents a unique way that scammers create a sense of urgency in their victims. By recognizing the underlying emotional, financial, legal, and social triggers, the **Urgency Detector** model can classify conversations and detect scam attempts based on how scammers manipulate their targets. Understanding these labels helps improve the model's ability to accurately categorize different scam scenarios and protect users from falling victim to fraudulent schemes.
