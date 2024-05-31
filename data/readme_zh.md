原始测评数据集以csv文件保存，第一行表示字段名，字段名因任务而异，后续每一行都代表一条测评数据。我们利用Huggingface的Datasets库实现测评数据集的自动化加载。

目前，我们支持文生文和文生图2类主流的大模型生成测评任务，测评数据集的字段名和解释如下所示：

|字段名|解释|
|---:|:--|
|prompt_text|输入的prompt文本|
|risk_type|prompt所属风险类别，详见risk_category.py|
|technique|攻击手法，若未用攻击手法，则为无|
|lang|promp_text所属语言，可为中文或英文|
|attack_type|（可选）L1，L2，L3或L4|
|||

**注意：promp_text必须存在。**

若要测评其他的任务，可参考上述测试数据集，设计相应的数据格式。