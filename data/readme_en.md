The original evaluation dataset is saved as a CSV file, where the first line represents the field names, which vary depending on the task, and each subsequent line represents a piece of evaluation data. We use the Datasets library from Huggingface to implement the automated loading of evaluation datasets.

Currently, we support two types of mainstream large model generation evaluation tasks: text-to-text and text-to-image. The field names and explanations of the evaluation dataset are as follows:

| Field Name | Explanation |
| ----------:|:------------|
| prompt_text | The input prompt text |
| risk_type | The risk category to which the prompt belongs, see risk_category.py for details |
| technique | Attack technique, if no attack technique was used, then it is none |
| lang | The language of the prompt_text, can be Chinese or English |
| attack_type | (Optional) L1, L2, L3, or L4 |
|||

**NOTE: prompt_text must exist.**

If you want to evaluate other tasks, you can refer to the above test dataset and design the corresponding data format.