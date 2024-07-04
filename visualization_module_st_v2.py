import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# 读取Excel数据
file_path = './data/snowball_model.xlsx'
df_500 = pd.read_excel(file_path, sheet_name='df_500')
df_1000 = pd.read_excel(file_path, sheet_name='df_1000')
point_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='point_knock_out_prob_500')
point_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='point_knock_out_prob_1000')
pe_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='pe_knock_out_prob_500')
pe_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='pe_knock_out_prob_1000')
pb_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='pb_knock_out_prob_500')
pb_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='pb_knock_out_prob_1000')
volatility_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='volatility_knock_out_prob_500')
volatility_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='volatility_knock_out_prob_1000')
df_500_knock_rate_dict = pd.read_excel(file_path, sheet_name='df_500_knock_rate_dict')
df_1000_knock_rate_dict = pd.read_excel(file_path, sheet_name='df_1000_knock_rate_dict')
df_500_current_loss_ratio_dict = pd.read_excel(file_path, sheet_name='df_500_current_loss_ratio_dict')
df_1000_current_loss_ratio_dict = pd.read_excel(file_path, sheet_name='df_1000_current_loss_ratio_dict')
day = df_500.iloc[-1,0].strftime('%Y年%m月%d日')
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


# 绘制函数 - 样本个数和有效样本数柱状图
def plot_data_combined(df, x_col, y_cols, title):
    fig = go.Figure()

    x = df[x_col]

    fig.add_trace(go.Bar(
        x=x,
        y=df[y_cols[0]],
        name=y_cols[0],
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=x,
        y=df[y_cols[1]],
        name=y_cols[1],
        marker_color='red'
    ))

    fig.update_layout(
        title=title,
        xaxis=dict(title=x_col),
        yaxis=dict(title='Sample Count'),
        barmode='group'
    )

    st.plotly_chart(fig)


# 绘制函数 - 敲出胜率线性图
def plot_knock_out_prob(df, x_col, y_col, title):
    fig = px.line(df, x=x_col, y=y_col, title=title, markers=True)
    st.plotly_chart(fig)


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
close_500 = df_500_knock_rate_dict.at[0, 'close']

point_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'point_knock_out_prob']
point_threshold_500 = df_500_knock_rate_dict.at[0, 'point_threshold']
pe_500 = df_500_knock_rate_dict.at[0, 'pe']
pe_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'pe_knock_out_prob']
pe_threshold_500 = df_500_knock_rate_dict.at[0, 'pe_threshold']
pb_500 = df_500_knock_rate_dict.at[0, 'pb']
pb_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'pb_knock_out_prob']
pb_threshold_500 = df_500_knock_rate_dict.at[0, 'pb_threshold']
volatility_500 = df_500_knock_rate_dict.at[0, 'volatility']
volatility_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'volatility_knock_out_prob']

close_1000 = df_1000_knock_rate_dict.at[0, 'close']
point_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'point_knock_out_prob']
point_threshold_1000 = df_500_knock_rate_dict.at[0, 'point_threshold']
pe_1000 = df_1000_knock_rate_dict.at[0, 'pe']
pe_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'pe_knock_out_prob']
pe_threshold_1000 = df_1000_knock_rate_dict.at[0, 'pe_threshold']
pb_1000 = df_1000_knock_rate_dict.at[0, 'pb']
pb_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'pb_knock_out_prob']
pb_threshold_1000 = df_1000_knock_rate_dict.at[0, 'pb_threshold']
volatility_1000 = df_1000_knock_rate_dict.at[0, 'volatility']
volatility_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'volatility_knock_out_prob']
pe_500_loss = df_500_current_loss_ratio_dict.at[0, "P/E"]
test_pe_500_loss = df_500_current_loss_ratio_dict.at[0, "test P/E"]
volatility_500_loss = df_500_current_loss_ratio_dict.at[0, "Volatility"]
test_volatility_500_loss = df_500_current_loss_ratio_dict.at[0, "test Volatility"]
loss_ratio_500 = df_500_current_loss_ratio_dict.at[0, "Loss Ratio"]

pe_1000_loss = df_1000_current_loss_ratio_dict.at[0, "P/E"]
test_pe_1000_loss = df_1000_current_loss_ratio_dict.at[0, "test P/E"]
volatility_1000_loss = df_1000_current_loss_ratio_dict.at[0, "Volatility"]
test_volatility_1000_loss = df_1000_current_loss_ratio_dict.at[0, "test Volatility"]
loss_ratio_1000 = df_1000_current_loss_ratio_dict.at[0, "Loss Ratio"]

knock_out_prob_description_500 = f"""
### 中证500指数
- 截止{day}，当前点位：**{close_500}**，点位敲出率：**{point_knock_out_prob_500}%**，参考阈值：**{point_threshold_500}**
- P/E: **{pe_500}**，P/E敲出率：**{pe_knock_out_prob_500}%**，参考阈值：**{pe_threshold_500}**
- P/B: **{pb_500}**，P/B敲出率：**{pb_knock_out_prob_500}%**，参考阈值：**{pb_threshold_500}**
- 波动率: **{volatility_500}%**，波动率敲出率：**{volatility_knock_out_prob_500}%**
"""

loss_ratio_description_500 = f"""
### 中证500当前点位历史亏损回测
- 回测P/E: **{pe_500_loss}**，实测P/E: **{test_pe_500_loss}**
- 波动率: **{volatility_500_loss}%**，实测波动率: **{test_volatility_500_loss}%**
- 历史回测亏损比例: **{loss_ratio_500}%**
"""

# 中证1000描述
knock_out_prob_description_1000 = f"""
### 中证1000指数
- 截止{day}，当前点位：**{close_1000}**，点位敲出率：**{point_knock_out_prob_1000}%**，参考阈值：**{point_threshold_1000}**
- P/E: **{pe_1000}**，P/E敲出率：**{pe_knock_out_prob_1000}%**，参考阈值：**{pe_threshold_1000}**
- P/B: **{pb_1000}**，P/B敲出率：**{pb_knock_out_prob_1000}%**，参考阈值：**{pb_threshold_1000}**
- 波动率: **{volatility_1000}%**，波动率敲出率：**{volatility_knock_out_prob_1000}%**
"""

loss_ratio_description_1000 = f"""
### 中证1000当前点位历史亏损回测
- 回测P/E: **{pe_1000_loss}**，实测P/E: **{test_pe_1000_loss}**
- 波动率: **{volatility_1000_loss}%**，实测波动率: **{test_volatility_1000_loss}%**
- 历史回测亏损比例: **{loss_ratio_1000}%**
"""

if index_option == '500':
    st.markdown(knock_out_prob_description_500)
    st.markdown(loss_ratio_description_500)
else:
    st.markdown(knock_out_prob_description_1000)
    st.markdown(loss_ratio_description_1000)

for title, df in df_map.items():
    st.subheader(title)

    # 样本个数和有效样本数柱状图
    st.write(f'{title} - 有效样本和敲出样本分布情况')
    plot_data_combined(df, x_col=df.columns[0], y_cols=['Total Samples', 'Valid Samples'],
                       title="")

    # 敲出胜率线性图
    st.write(f'{title} - 敲出概率分布')
    plot_knock_out_prob(df, x_col=df.columns[0], y_col='Knockout Probability',
                        title="")

    # 显示数据表
    st.write(df)
