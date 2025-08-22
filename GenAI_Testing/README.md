
GenAI_Testing/  
Datasets/ # contains GenAI datasets  
├── Adversarial_SMS_Dataset.txt # Dataset with Threat-actor or Hacker realted artifacts  
├── New_SMS_Dataset.txt # Dataset similar to training corpus but with different messages and even stricter class imbalance.  
Notebooks/ # Notebook used for examing models on new datasets  
├── New_SMS_Testing.ipynb # Models are tested/compared on new GenAI datasets  
Prompts/ # contains prompts used to make datasets  
├── Adversarial_Spam_Prompt.txt # prompt used to make threat-actor dataset  
├── Prompt_new_SMS_Dataset.txt # prompt used to make similar dataset to training corpus.  
Scripts/ # Contains script used to Preprocess datasets  
├── Spam_Preprocessor.py # Preprocesses new datasets for model testing  
