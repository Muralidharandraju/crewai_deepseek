#!/bin/bash

# Variables
model_name="deepseek-r1:1.5b"
custom_model_name="crewai-deepseek-r1"

#FILE_PATH="D:/Code/crewai_opensource/setup/llama3Modelfile"

# Get the base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f deepseekModelfile