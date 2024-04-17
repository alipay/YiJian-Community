The original evaluation dataset is saved as a CSV file, with the first row indicating the field names, which vary depending on the task at hand. Each subsequent row represents a piece of evaluation data. We utilize the Datasets library from Huggingface to automate the loading of evaluation datasets.

Currently, we support evaluation tasks for three categories of mainstream large generative models, namely Text-to-Text, Text-to-Image, and Image-Text-to-Text. The field names and explanations for each type of task are as follows:

- **Text-to-Text**

| Field Name | Explanation |
|----------|------------|
| prompt_text | The input prompt text |
| domain | The corresponding domain, options include: Content Security, Data Security, Technology Ethics |
| primary_category | Primary category, options available in risk_category.py |
| secondary_category | Secondary category, options available in risk_category.py |
|||

- **Text-to-Image**

| Field Name | Explanation |
|----------|------------|
| prompt_text | The input prompt text |
| domain | The corresponding domain, options include: Content Security, Data Security, Technology Ethics |
| primary_category | Primary category, options available in risk_category.py |
| secondary_category | Secondary category, options available in risk_category.py |
|||

- **Image-Text-to-Text**

| Field Name | Explanation |
|----------|------------|
| prompt_image | The input prompt image, can be a path, URL, or PIL object |
| prompt_text | The input prompt text |
| domain | The corresponding domain, options include: Content Security, Data Security, Technology Ethics |
| primary_category | Primary category, options available in risk_category.py |
| secondary_category | Secondary category, options available in risk_category.py |
|||

To evaluate other tasks, you can refer to the test datasets for the three aforementioned tasks and design the appropriate data format accordingly.