# Create a Wasm-based LLM app for financial analysts
As part of application process, I have completed the pre-test mentioned in the project description and submitted the same in the Cover Letter with all other required documents. 

```
System Specification
Processor: Intel i5 - 12th generation 
RAM: 12 GB 
Operating System: Ubuntu WSL

Note: If higher spec system is required at any time in the mentorship period, I have access to 32 GB RAM PC build with dedicated GPU
```
## Pre-test 1
Follow [instructions](https://docs.gaianet.ai/node-guide/quick-start/) to create and deploy a Gaia node, which is contains an LLM, an embedding model, and a vector database snapshot.
### Solution
I followed the guide and was able to deploy a Gaia node, which contained [Qwen2-0.5](https://github.com/GaiaNet-AI/node-configs/tree/main/qwen2-0.5b-instruct) model, Nomic-embed-text-v1.5-Embedding-GGUF and knowledge base of Paris

> Chat with the deployed Gaia node
<img width="690" alt="image" src="https://github.com/user-attachments/assets/2b28adfe-9110-41ec-a2ca-34a17c78cc4e">
<img width="690" alt="image" src="https://github.com/user-attachments/assets/76981031-405d-43cc-97ca-b182d0dc0639">

---
## Pre-test 2
[Choose one of the tutorials](https://docs.gaianet.ai/category/knowledge-bases) to create a vector snapshot from your own documents, and update the Gaia node with the new snapshot.
### Solution 
For this task, I created a vector snapshot using this blog [Build an llm from scratch](https://blog.spheron.network/how-to-build-an-llm-from-scratch-a-step-by-step-guide) and converted this into a plain text file and followed this [tutorial](https://docs.gaianet.ai/creator-guide/knowledge/text) to create a vector snapshot from it. The compressed vector snapshot is available at [huggingface](https://huggingface.co/datasets/angadsinghh/create_llm_from_scratch/tree/main). Then I updated the Gaia node with newly created vector snapshot.

- Updated config.json - [link](https://github.com/angad-singhh/Mentorship-Pretest/blob/main/config.json)
- New vector snapshot - [link](https://github.com/angad-singhh/Mentorship-Pretest/blob/main/my.snapshot.tar.gz)

```
NOTE:
In previous task, the deployed Gaia node had default knowledge base and then I updated the same with new knowledge base on the topic about building and LLM from scratch. So, For this task I asked the same question in the chat BEFORE updating the vector snapshot and AFTER updating the vector snapshot
```
<br>

**Below is the Updated node**

<img width="500" alt="image" src="https://github.com/user-attachments/assets/9f79a2ea-6880-470f-8707-387a653c51bf">

<br> 
<br>

**Below is the Response before updating the knowledge base**

<img width="495" alt="Screenshot 2024-08-13 010136" src="https://github.com/user-attachments/assets/e77c6781-042d-49b4-8926-72b121636737">

<br>
<br>

**Below is the Respose after updating the knowledge**

<img width="778" alt="image" src="https://github.com/user-attachments/assets/da3deebc-4d89-45b5-b0b9-494aec026fa7">

<br>

**Why different results ?**

Updating the knowledge base and system prompt, provided the llm model an additional context about the domain from which to answer, which resulted in different answer compared with one with default knowledge base.

---
## End Note
With this I have completed both the pre-test required and I'm really looking forward to work on this project. 

Thanks, Angad Singh

