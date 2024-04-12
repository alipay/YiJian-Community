原始测评数据集以csv文件保存，第一行表示字段名，字段名因任务而异，后续每一行都代表一条测评数据。我们利用Huggingface的Datasets库实现测评数据集的自动化加载。

目前，我们支持文生文、文生图和图生文共3类主流的大模型生成测评任务，各类任务的字段名和解释如下所示：

- **文生文**

|字段名|解释|
|---:|:--|
|prompt_text|输入的prompt文本|
|domain|所属领域，可选项：内容安全、数据安全、科技伦理|
|primary_category|一级目录，可选项见risk_category_zh.json|
|secondary_category|二级目录，可选项见risk_category_zh.json|
|response_text|存储大模型预测后返回的文本|
|||

- **文生图**

|字段名|解释|
|---:|:--|
|prompt_text|输入的prompt文本|
|domain|所属领域，可选项：内容安全、数据安全、科技伦理|
|primary_category|一级目录，可选项见risk_category_zh.json|
|secondary_category|二级目录，可选项见risk_category_zh.json|
|response_image|存储大模型预测后返回的图像，可为路径、url或PIL对象|
|||

- **图生文**

|字段名|解释|
|---:|:--|
|prompt_image|输入的prompt图像，可为路径、url或PIL对象|
|prompt_text|输入的prompt文本|
|domain|所属领域，可选项：内容安全、数据安全、科技伦理|
|primary_category|一级目录，可选项见risk_category_zh.json|
|secondary_category|二级目录，可选项见risk_category_zh.json|
|response_text|存储大模型预测后返回的文本|
|||

若要测评其他的任务，可参考上述三种任务的测试数据集，设计相应的数据格式。