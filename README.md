# Backup System Dynamic Tag Generation modules
## Overview
This repository hosts machine learning scripts for dynamic tag generation in a Backup System, enhancing storage, retrieval performance, and sensitive data protection.

### Key Components:
- **AbstractiveSummarizer.py**: Uses the Pegasus model from the Hugging Face library to generate abstractive summaries, which can condense large texts into concise, informative summaries.
- **ImageClassification.py**: Employs OpenCV's deep learning features to classify objects within images. It's suitable for tagging images based on their content.
- **Video_Classification.py**: Extends the object classification capability to video streams, identifying and tagging objects in real-time or recorded videos.
- **fileConverter.py**: A versatile tool for converting files from formats like DOCX, PDF, CSV, XLSX, and images to text, enabling text-based processing and analysis.
- **keybertextracter.py**: Leverages the DistilBERT model for keyword extraction, identifying key terms in texts which helps categorize and summarize content.
- **piidata.py**: Uses advanced NLP techniques to identify and categorize personally identifiable information (PII) in texts, essential for data privacy and compliance.
  
### Usage
Each script can be independently utilized based on the specific needs of the Backup System:

- **Text Summarization** (`AbstractiveSummarizer.py`): Generate concise summaries of large documents, useful for quick reviews and content digestion.

- **Image Classification** (`ImageClassification.py`): Categorize and tag images based on their content, aiding in efficient image data management and retrieval.

- **Video Classification** (`Video_Classification.py`): Apply object classification to video streams, identifying and tagging objects in real-time or recorded videos for enhanced video data sorting and indexing.

- **File Conversion** (`fileConverter.py`): Standardize various file formats (DOCX, PDF, CSV, XLSX, images) into text, facilitating uniform text-based processing and analysis.

- **Keyword Extraction** (`keybertextracter.py`): Extract key terms from texts to identify main themes or topics, assisting in content categorization and summarization.

- **PII Detection** (`piidata.py`): Identify and categorize personally identifiable information (PII) in texts, crucial for maintaining data privacy and compliance.

### Contributing

We welcome contributions. Please submit pull requests for any improvements or bug fixes.
