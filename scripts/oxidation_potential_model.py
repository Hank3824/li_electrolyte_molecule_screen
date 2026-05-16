from unimol_tools import MolTrain, MolPredict
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# clf = MolTrain(
#     task='regression',
#     model_name='unimolv2',  # use the larger model
#     model_size='164m',
#     epochs=200,
#     learning_rate=2e-4,  
#     batch_size=32,
#     early_stopping=15,
#     metrics='mae',
#     split='random',  # scaffold split may be more appropriate than random split
#     kfold=5,
#     save_path=r'/home/hank/code/unimol_tools/Result/Oxidation Potential',
# )
# train_op_file_path = r'/home/hank/code/unimol_tools/dataset/Oxidation Potential/train_op_set.csv'

# # Train the model
# clf.fit(data = train_op_file_path)

# Load the trained predictor
clf = MolPredict(load_model = r'/home/hank/code/unimol_tools/Result/Oxidation Potential')
# train_op_file_path = r'/home/hank/code/unimol_tools/dataset/Oxidation Potential/train_op_set.csv'
# test_op_file_path = r'/home/hank/code/unimol_tools/dataset/Oxidation Potential/test_op_set.csv'

# predict_train = clf.predict(data = train_op_file_path)
# predict_test = clf.predict(data = test_op_file_path)

# # Read predictions and ground-truth values
# train_df = pd.read_csv(train_op_file_path)
# test_df = pd.read_csv(test_op_file_path)

# target_column = 'TARGET_Oxidation Potential (vs Li/Li+)'
# true_values_train = train_df[target_column]
# true_values_test = test_df[target_column]

# predict_values_train = predict_train.flatten()
# predict_values_test = predict_test.flatten()

# results_train_df = pd.DataFrame({
#     'True Values': true_values_train,
#     'Predicted Values': predict_values_train
# })
# results_test_df = pd.DataFrame({
#     'True Values': true_values_test,
#     'Predicted Values': predict_values_test
# })

# output_train_path = r'/home/hank/code/unimol_tools/predict dataset/Oxidation Potential/train_predict.csv'
# output_test_path = r'/home/hank/code/unimol_tools/predict dataset/Oxidation Potential/test_predict.csv'
# results_train_df.to_csv(output_train_path, index=False)
# results_test_df.to_csv(output_test_path, index=False)

####################################################### SMILES ONLY ########################################################

# Path to the SMILES-only dataset
smiles_only_file_path = r'/home/hank/code/unimol_tools/dataset/to_predict/smiles_only_file_cleaned.csv'
# Run prediction
predict_smiles_only = clf.predict(data = smiles_only_file_path)

# Read the original SMILES data
smiles_df = pd.read_csv(smiles_only_file_path)
predict_values_smiles_only = predict_smiles_only.flatten()

# Create a result DataFrame containing SMILES and predicted values
results_smiles_df = pd.DataFrame({
    'SMILES': smiles_df['SMILES'],  # Assumes the SMILES column is named'SMILES'
    'Predicted Oxidation Potential': predict_values_smiles_only
})


# Save prediction results
output_smiles_path = r'/home/hank/code/unimol_tools/dataset/to_predict/Oxidation Potential/predict_op.csv'
results_smiles_df.to_csv(output_smiles_path, index=False)

print(f"Prediction completed. Results saved to: {output_smiles_path}")
print(f"Predicted {len(predict_values_smiles_only)} molecules")

