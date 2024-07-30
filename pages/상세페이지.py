import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

def display_recommendation_page_():
    # Query params에서 선택한 값 가져오기
    choice1 = st.query_params.get('choice1', [''])[0]
    selected_sectors = st.query_params.get('sectors', [])
    
    # 올바른 파일 경로로 수정
    file_path = "df_0702.csv"
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("CSV 파일을 찾을 수 없습니다. 파일 경로를 확인해 주세요.")
        return
    st.dataframe(df)


if __name__ == "__main__":
    display_recommendation_page_()