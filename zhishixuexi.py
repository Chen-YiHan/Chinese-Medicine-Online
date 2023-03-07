import json
from pathlib import Path
import random

import streamlit as st

import get


def dis(page):
        name, zhongzhi, paozhi, yaoxing, zhizhu = get.get_page(page)
        st.header(name)
        st.subheader("种植")
        f"{zhongzhi.replace('<br>', '')}"
        st.subheader("炮制")
        f"{paozhi.replace('<br>', '')}"
        st.subheader("药性")
        f"{yaoxing.replace('<br>', '')}"
        st.subheader("植株")
        f"{zhizhu.replace('<br>', '')}"
        if Path(f"./120image/zhizhu/{name}.jpg").exists():
            zhizhu_img = st.image(f"./120image/zhizhu/{name}.jpg")
        if Path(f"./120image/chengyao/{name}.jpg").exists():
            chengyao_img = st.image(f"./120image/chengyao/{name}.jpg")
        




st.header("中药材知识学习")
"*包罗8000余种中药材的知识宝库，附图数百张倾力之作*"
st.markdown("本软件代码由陈一翰[@Chen-YiHan](https://github.com/Chen-YiHan)制作，方利国老师指导")
if 'page' not in st.session_state:
	st.session_state.page = 0
	#dis(st.session_state.page)
#dis(st.session_state.page)
if st.button(f"上一页"):
    st.session_state.page -= 1
    #dis(st.session_state.page)
if st.button(f"下一页"):
    #print(1)
    st.session_state.page += 1
    #dis(st.session_state.page)
dis(st.session_state.page)

#st.write('Count = ', st.session_state.page)