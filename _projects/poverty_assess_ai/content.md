## Project Overview {#overview}

Fine tuned Llama 3.2 1B to classify a household's poverty status given a description.

## What did I do? {#project-explanation}

### 1. Data {#getting-data}
[(MHS & DHS) Multidimensional Poverty Index](https://hdr.undp.org/content/2024-global-multidimensional-poverty-index-mpi#/indicies/MPI)
[Poverty Stoplight](https://www.povertystoplight.org/)

### 2. Convert to natural language. {#data-cleaning}
The data was stored in a .csv file, so we made a script that converted this data to sentences. For example if a column 'clean_water_access' is 0, the sentence would be 'The household does not have access to clean water.' otherwise it would be 'The household has access to clean water.'.

So we concatenated a bunch of these sentences into one paragraph for each household. Then the target output for the model would be "normal", "vulnerable", "poor", or "extremely poor" depending on the score in the database.

### 3. Fine tune model
Used [SFTTrainer](https://huggingface.co/docs/trl/main/en/sft_trainer) to fine tune the model on the prepared data. Fine tuning took roughly a day.

### 4. Test model
Tested the model on a separate test set.

Detailed Metrics:
- normal: TP=4994, FP=26, FN=13, TN=2943, Precision=0.995, Recall=0.997, F1=0.996  
- vulnerable: TP=262, FP=8, FN=12, TN=7694, Precision=0.970, Recall=0.956, F1=0.963  
- poor: TP=2628, FP=4, FN=8, TN=5336, Precision=0.998, Recall=0.997, F1=0.998  
- extremely poor: TP=53, FP=1, FN=6, TN=7916, Precision=0.981, Recall=0.898, F1=0.938  

Overall Metrics:  
- Accuracy: 0.995  
- Precision: 0.986  
- Recall: 0.962  
- F1 Score: 0.974  

### 5. Create demo website for model
Using flask I created a website that interfaces with the model via Ollama.  
[Poverty Assessment AI](http://poverty-assess-ai.wpi.edu/about)