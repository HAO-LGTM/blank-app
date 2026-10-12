import streamlit as st
import json
import base64
from PIL import Image
from io import BytesIO

# ===================== 页面全局配置（国风深色主题，适配大赛）=====================
st.set_page_config(
    page_title="文脉信号 | Cultural Signal",
    page_icon="🎐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS：深色国风样式
st.markdown("""
<style>
    .stApp {
        background-color: #0f0f11;
        color: #f0f0f0;
    }
    .title-text{
        color:#c41e3a;
        font-size:42px;
        font-weight:bold;
    }
    .sub-title{
        color:#d4af37;
        font-size:18px;
    }
    .card{
        background:#1a1a1d;
        padding:20px;
        border-radius:12px;
        border:1px solid #c41e3a60;
    }
</style>
""",unsafe_allow_html=True)

# ===================== 【模块1：文化信号解析 模拟大模型输出】=====================
def parse_culture_signal(input_topic):
    """输入文化主题，返回结构化文化标签（模拟LLM语义编码）"""
    case_dict = {
        "敦煌飞天":{
            "时代":"唐代",
            "元素":["飘带","莲花","佛教艺术","飞天姿态"],
            "色彩":["朱砂红","石青","金色"],
            "情感":["自由","祥和","升华"],
            "prompt":"未来通信风格，敦煌飞天数字使者，赛博敦煌，飘逸飘带，鎏金纹饰，国风科幻，高清插画"
        },
        "青花瓷 × 智慧城市":{
            "时代":"元明",
            "元素":["青花缠枝纹","瓷胎","山水纹样","亭台"],
            "色彩":["钴蓝","瓷白"],
            "情感":["清雅、宁静、生生不息"],
            "prompt":"青花瓷纹样融合未来智慧城市，数字中国风城市，青蓝瓷纹建筑，流光粒子，宏大场景"
        },
        "山东剪纸 × 智慧传播":{
            "时代":"齐鲁民间非遗",
            "元素":["剪纸纹样、花鸟、祥云、鲁地民俗"],
            "色彩":["中国红、米白"],
            "情感":["质朴、热烈、传承"],
            "prompt":"山东剪纸非遗，数字粒子剪纸，国风，花鸟祥云，红色剪纸，赛博数字展厅"
        },
        "兵马俑 × 元宇宙":{
            "时代":"秦代",
            "元素":["甲胄、陶俑阵列、青铜兵器、秦式纹样"],
            "色彩":["陶土灰、青铜绿"],
            "情感":["厚重、雄浑、文明延续"],
            "prompt":"兵马俑元宇宙数字阵列，秦甲胄融合数字流光，宏大史诗场景"
        }
    }
    if input_topic in case_dict:
        return case_dict[input_topic]
    else:
        # 通用返回
        return {
            "时代":"未知",
            "元素":["传统文化元素"],
            "色彩":["传统色系"],
            "情感":["文化传承"],
            "prompt":"国风数字艺术，传统文化与AI未来融合"
        }

# ===================== 侧边栏导航 =====================
with st.sidebar:
    st.markdown("<p class='title-text'>🎐 文脉信号</p>",unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>基于多模态生成AI的中华文化数字传播系统</p>",unsafe_allow_html=True)
    page = st.radio("功能导航", ["文化信号解析器","AI视觉生成展厅","作品介绍"])

# ===================== 页面1：文化信号解析器 =====================
if page == "文化信号解析器":
    st.markdown("<h1 class='title-text'>📡 文化信号解析</h1>",unsafe_allow_html=True)
    st.write("将中华传统文化作为「文化信号」，完成语义编码、文化元素提取")

    col1, col2 = st.columns([1,1])
    with col1:
        user_input = st.text_input("输入文化主题",value="敦煌飞天")
        submit_btn = st.button("🔍 解析文化信号",type="primary")
    with col2:
        st.markdown("<div class='card'>",unsafe_allow_html=True)
        st.write("示例选题：")
        st.write("- 敦煌飞天")
        st.write("- 青花瓷 × 智慧城市")
        st.write("- 山东剪纸 × 智慧传播")
        st.write("- 兵马俑 × 元宇宙")
        st.markdown("</div>",unsafe_allow_html=True)

    if submit_btn:
        res = parse_culture_signal(user_input)
        st.divider()
        st.markdown("<h3 style='color:#d4af37'>✅ 文化信号编码结果</h3>",unsafe_allow_html=True)
        c1,c2,c3,c4 = st.columns(4)
        with c1:
            st.markdown("<div class='card'>",unsafe_allow_html=True)
            st.subheader("时代")
            st.write(res["时代"])
            st.markdown("</div>",unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='card'>",unsafe_allow_html=True)
            st.subheader("核心元素")
            for item in res["元素"]:
                st.write(f"- {item}")
            st.markdown("</div>",unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='card'>",unsafe_allow_html=True)
            st.subheader("色彩谱系")
            for item in res["色彩"]:
                st.write(f"- {item}")
            st.markdown("</div>",unsafe_allow_html=True)
        with c4:
            st.markdown("<div class='card'>",unsafe_allow_html=True)
            st.subheader("文化情感")
            for item in res["情感"]:
                st.write(f"- {item}")
            st.markdown("</div>",unsafe_allow_html=True)

        st.markdown("<div class='card'>",unsafe_allow_html=True)
        st.subheader("🎨 送入AIGC的生成Prompt")
        st.code(res["prompt"],language="text")
        st.markdown("</div>",unsafe_allow_html=True)
        st.info("下一步：将该结构化Prompt送入图像生成模型，生成视觉作品，进入数字展厅。")

# ===================== 页面2：AI视觉生成展厅 =====================
elif page == "AI视觉生成展厅":
    st.markdown("<h1 class='title-text'>🖼️ 数字文化展厅</h1>",unsafe_allow_html=True)
    st.write("文化信号完成视觉转换，生成可传播的数字文创作品")

    gallery_case = st.selectbox("选择展厅作品",["敦煌飞天 × 未来通信","青花瓷 × 智慧城市","山东剪纸 × 智慧传播","兵马俑 × 元宇宙"])
    st.divider()
    st.markdown("<div class='card'>",unsafe_allow_html=True)
    st.subheader(gallery_case)
    st.write("【Demo提示】正式版本此处调用AIGC接口实时生成图片，当前演示预留图片显示区域")
    st.image("https://picsum.photos/id/1035/1200/600",caption="AI生成文化视觉作品（替换为你自己生成的国风图片）",use_container_width=True)
    st.markdown("</div>",unsafe_allow_html=True)

    col_share1,col_share2 = st.columns(2)
    with col_share1:
        st.button("📤 生成分享二维码",type="secondary")
    with col_share2:
        st.download_button("💾 导出作品说明文档",data="作品介绍文本",file_name=f"{gallery_case}.txt")

# ===================== 页面3：作品介绍（用于答辩演示） =====================
elif page == "作品介绍":
    st.markdown("<h1 class='title-text'>《文脉信号》系统介绍</h1>",unsafe_allow_html=True)
    st.markdown("<div class='card'>",unsafe_allow_html=True)
    st.markdown("""
### 核心创意
将中华传统文化视为一种**文化信号**，利用人工智能完成文化语义编码、视觉生成和数字传播，实现传统文化从**文本信号到视觉信号**的智能转换。

### 技术链路
`用户输入文化主题` → `大模型语义理解 & 文化元素提取` → `结构化文化信号编码` → `AIGC视觉生成` → `Web数字展厅与传播`

### 三大创新点
1. **文化信号转换模型**：把文化传播抽象成通信链路（信息编码-传输-可视化解码），贴合通信工程背景
2. **文化语义驱动AIGC**：不是简单文生图，先解析文化本体要素，再生成，保证文化准确性
3. **面向青年的数字文化传播新模式**：轻量化Web展厅，一键分享，降低传统文化传播门槛
""")
    st.markdown("</div>",unsafe_allow_html=True)
