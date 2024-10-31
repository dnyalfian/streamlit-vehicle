import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import tree
import streamlit as st

from web_maintenance import train_model

def app(df, x, y):

    ##warnings.filterwarnings('ignore')
    
    st.title("Visualisasi Prediksi Services Kendaraan")

    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x, y)
        disp = ConfusionMatrixDisplay.from_estimator(model, x, y, display_labels=['1', '0'])
        disp.plot(cmap=plt.cm.Oranges)
        st.pyplot()


    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x,y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['1','0']
        )

        st.graphviz_chart(dot_data)