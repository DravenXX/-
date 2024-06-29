#不适用sns库以便部署到云端
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 读取Excel数据
file_path = 'data/snowball_model.xlsx'
point_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='point_knock_out_prob_500')
point_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='point_knock_out_prob_1000')
pe_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='pe_knock_out_prob_500')
pe_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='pe_knock_out_prob_1000')
pb_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='pb_knock_out_prob_500')
pb_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='pb_knock_out_prob_1000')
volatility_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='volatility_knock_out_prob_500')
volatility_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='volatility_knock_out_prob_1000')


# 将数据框的列名转换为英文
def rename_columns(df):
    df.columns = ['Metric', 'Total Samples', 'Valid Samples', 'Knockout Probability']
    return df


point_knock_out_prob_500 = rename_columns(point_knock_out_prob_500)
point_knock_out_prob_1000 = rename_columns(point_knock_out_prob_1000)
pe_knock_out_prob_500 = rename_columns(pe_knock_out_prob_500)
pe_knock_out_prob_1000 = rename_columns(pe_knock_out_prob_1000)
pb_knock_out_prob_500 = rename_columns(pb_knock_out_prob_500)
pb_knock_out_prob_1000 = rename_columns(pb_knock_out_prob_1000)
volatility_knock_out_prob_500 = rename_columns(volatility_knock_out_prob_500)
volatility_knock_out_prob_1000 = rename_columns(volatility_knock_out_prob_1000)


# 绘制函数
def plot_data_combined(df, x_col, y_cols, title):
    fig, ax = plt.subplots(figsize=(14, 7))

    x = np.arange(len(df[x_col]))  # x轴位置
    width = 0.4  # 每个柱的宽度

    ax.bar(x - width / 2, df[y_cols[0]], width, label=y_cols[0], color='blue', alpha=0.6)
    ax.bar(x + width / 2, df[y_cols[1]], width, label=y_cols[1], color='red', alpha=0.6)

    ax.set_xticks(x[::len(x) // 10])  # 每隔一定数量显示一个标签
    ax.set_xticklabels(df[x_col][::len(x) // 10])

    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel('Sample Count')
    ax.legend()

    st.pyplot(fig)


# 绘制函数 - 敲出胜率线性图
def plot_knock_out_prob(df, x_col, y_col, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df[x_col], df[y_col], marker='o')
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

# Streamlit应用
st.title('雪球产品敲出率分析')

# 选择数据框
index_option = st.selectbox(
    'Select Index',
    ('500', '1000'))

# 根据选择映射数据框
if index_option == '500':
    df_map = {
        'Point Knock Out Probability': point_knock_out_prob_500,
        'PE Knock Out Probability': pe_knock_out_prob_500,
        'PB Knock Out Probability': pb_knock_out_prob_500,
        'Volatility Knock Out Probability': volatility_knock_out_prob_500
    }
else:
    df_map = {
        'Point Knock Out Probability': point_knock_out_prob_1000,
        'PE Knock Out Probability': pe_knock_out_prob_1000,
        'PB Knock Out Probability': pb_knock_out_prob_1000,
        'Volatility Knock Out Probability': volatility_knock_out_prob_1000
    }
# 显示计算结果
result_text = """
当前中证500指数点位：4942.78, 点位敲出率：100.0%\n
P/E: 21.2, P/E敲出率：81.48%\n
P/B: 1.5567, P/B敲出率：100.0%\n
波动率: 24.87%, 波动率敲出率：94.74%\n
当前中证1000指数点位：4895.99, 点位敲出率：100.0%\n
P/E: 31.59, P/E敲出率：65.38%\n
P/B: 1.7054, P/B敲出率：100.0%\n
波动率: 30.88%, 波动率敲出率：13.33%\n
当前回测P/E: 26.82, 波动率: 20.32%, 历史回测亏损比例: 5.57%\n
当前回测P/E: 39.91, 波动率: 20.35%, 历史回测亏损比例: 14.37%\n
"""
st.markdown(result_text)
# 遍历所有数据框并显示图表和数据
for title, df in df_map.items():
    st.subheader(title)

    # 样本个数和有效样本数柱状图
    st.write(f'{title} - Sample and Knock Out Samples Distribution')
    plot_data_combined(df, x_col=df.columns[0], y_cols=['Total Samples', 'Valid Samples'],
                       title=f'{title} - Sample Count and Valid Samples Distribution')

    # 敲出胜率线性图
    st.write(f'{title} - Knockout Probability Distribution')
    plot_knock_out_prob(df, x_col=df.columns[0], y_col='Knockout Probability',
                        title=f'{title} - Knockout Probability Distribution')

    # 显示数据表
    st.write(df)
