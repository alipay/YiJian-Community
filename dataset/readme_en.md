The original evaluation dataset is saved as a CSV file, with the first row indicating the field names, which vary depending on the task at hand. Each subsequent row represents a piece of evaluation data. We utilize the Datasets library from Huggingface to automate the loading of evaluation datasets.

Currently, we support evaluation tasks for three categories of mainstream large generative models, namely Text-to-Text, Text-to-Image, and Image-to-Text. The field names and explanations for each type of task are as follows:

- **Text-to-Text**
  
| Field Name | Explanation |
|----------|------------|
| prompt_text | The input prompt text |
| domain | The corresponding domain, options include: Content Security, Data Security, Technology Ethics |
| primary_category | Primary category, options available in risk_category_en.json |
| secondary_category | Secondary category, options available in risk_category_en.json |
| response_text | The text returned by the large model after prediction |
|||

- **Text-to-Image**
  
| Field Name | Explanation |
|----------|------------|
| prompt_text | The input prompt text |
| domain | The corresponding domain, options include: Content Security, Data Security, Technology Ethics |
| primary_category | Primary category, options available in risk_category_en.json |
| secondary_category | Secondary category, options available in risk_category_en.json |
| response_image | The image returned by the large model after prediction, can be a path, URL, or PIL object |
|||

- **Image-to-Text**
  
| Field Name | Explanation |
|----------|------------|
| prompt_image | The input prompt image, can be a path, URL, or PIL object |
| prompt_text | The input prompt text |
| domain | The corresponding domain, options include: Content Security, Data Security, Technology Ethics |
| primary_category | Primary category, options available in risk_category_en.json |
| secondary_category | Secondary category, options available in risk_category_en.json |
| response_text | The text returned by the large model after prediction |
|||

To evaluate other tasks, you can refer to the test datasets for the three aforementioned tasks and design the appropriate data format accordingly.