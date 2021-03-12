
from transformers import TFBertModel,  BertConfig, BertTokenizerFast
from tensorflow.keras.layers import Input, Dropout, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf



import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--review",type=str, required=True,
  help="review text")
ap.add_argument("-m", "--model", required=True,
  help="path to model")
args = vars(ap.parse_args())


MODEL_NAME = 'bert-base-uncased'
category_label = ["food","service"]
config = BertConfig.from_pretrained(MODEL_NAME)
config.output_hidden_states = False
MAX_LENGTH = 100
config = BertConfig.from_pretrained(MODEL_NAME)
config.output_hidden_states = False
tokenizer = BertTokenizerFast.from_pretrained(pretrained_model_name_or_path = MODEL_NAME, config = config)
# Load the Transformers BERT model
transformer_model = TFBertModel.from_pretrained(MODEL_NAME, config = config)
model = tf.keras.models.load_model(args["model"])



def predict_review(): 
    # Ready test data
	test_y_food = to_categorical(data_test['food_label'])
	test_y_service = to_categorical(data_test['service_label'])

	test_x = tokenizer(
	    text=[args["review"]],
	    add_special_tokens=True,
	    max_length=MAX_LENGTH,
	    truncation=True,
	    padding=True, 
	    return_tensors='tf',
	    return_token_type_ids = False,
	    return_attention_mask = False,
	    verbose = True)

	prediction = model.predict(test_x["input_ids"][0])
	output_dict =  { "category_label": category_label,
	  "category_result": [prediction["food"][:, 1].max()> 0,  prediction["service"][:, 1].max()> 0],
	  "category_score": [prediction["food"][:, 1].max(),prediction["service"][:, 1].max()]
	}
	return output_dict
    
     
if args["review"]:
   print(predict_review())

