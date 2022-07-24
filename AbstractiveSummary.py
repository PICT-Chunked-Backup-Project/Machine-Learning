# =========================LIBRARY SETUP=====================================

# use python 3.9
# pip install torch
# pip install --upgrade tensorflow
# verify tf install by running python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
# pip install flax
# pip install transformers
# pip install sentencepiece



from copyreg import constructor
from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from transformers import pipeline
import os


class AbstractiveSummarizer:
    text=""
    def __init__(self,t):
        text=t


    def getSummary(self):
        wordList=self.text.split()
        str=""
        opstr=""
        counter=0
        finalCounter=0
        for word in wordList:
            str=str+word
            finalcounter=finalcounter+1
            if(finalCounter>=1200):
                break
            counter=counter+1
            if counter>=400:
                opstr=opstr+Summary(str)
                counter=0
                str=""
        opstr=opstr+Summary(str)     
        return opstr 
        

def Summary(example_text):

    # Pick model
    model_name = "google/pegasus-xsum"

    # Load pretrained tokenizer
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

    # example_text = """When the UK government imposed sanctions on Oleg Deripaska, they described him as worth £2bn and a "one-time business partner" of Roman Abramovich.
    #
    # In early March, a court heard that he has a multi-million pound property portfolio in the UK, including the art deco mansion Hamstone House in Weybridge, Surrey. Sitting in eight acres of grounds, the Grade II listed property was acquired for £7.1m by a Cyprus-based company, Edenfield Investments Limited, in 2001.
    #
    # Mr Deripaska also owns a large home in Belgrave Square that was occupied by protestors. However, a spokesman for the billionaire at the time said the property belonged to family members.
    #
    # There is evidence suggesting Mr Deripaska owns a building five minutes' walk from Buckingham Palace. The 17th-Century terrace house was bought in 2004 for £4.7m by Astibe Limited - an offshore shell company incorporated in the British Virgin Islands, which appears in the annual accounts of EN+ (an energy and metals group that Mr Deripaska has a stake in). The property is listed as the address of the company, according to research by Transparency International.
    #
    # A judge has frozen UK bank accounts operated by a British businessman amid allegations they are linked to Mr Deripaska - National Crime Agency investigators believe the accounts were being used to help the oligarch avoid sanctions.
    #
    # A spokesperson for Mr Deripaska said the sanctions were "deeply misguided" and based on "unfounded and hollow accusations".
    #
    # "Mr Deripaska has never been involved in politics. It is wrong to suggest that Mr Deripaska is close to the Government of Russia and/or Vladimir Putin," the statement read.
    #
    # "The decision to sanction him has nothing to do with justice or law, neither does the freezing of assets belonging to him or his family."""

    # Define PEGASUS model
    pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

    # Create tokens
    tokens = pegasus_tokenizer(example_text, truncation=True, padding="longest", return_tensors="pt")

    # Summarize text
    encoded_summary = pegasus_model.generate(**tokens)

    # Decode summarized text
    decoded_summary = pegasus_tokenizer.decode(
        encoded_summary[0],
        skip_special_tokens=True
    )

    # Define summarization pipeline
    summarizer = pipeline(
        "summarization",
        model=model_name,
        tokenizer=pegasus_tokenizer,
        framework="pt"
    )

    # Create summary
    summary = summarizer(example_text, min_length=30, max_length=150)

    return(f"Summarized Text: {summary[0]['summary_text']}")


    

