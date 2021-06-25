import streamlit as st
import streamlit.components.v1 as components
import base64
from PIL import Image



def app():
    st.title(' ')
    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

    set_background('Front.jpg')

    new_title = '<p style="font-family:Fjord One; color:Black; font-size: 42px;"><b>One Stop solution for all the skin related diseases</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Fjord One; color:Red; font-size: 42px;"><b>About Gloww:</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Sans One; color:Black; font-size: 32px;"><b>The skin is the largest organ of the body, with a total area of about 20 square feet. The skin protects us from microbes and the elements, helps regulate body temperature, and permits the sensations of touch, heat, and cold.<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Sans One; color:Black; font-size: 32px;"><b>Gloww is a website that Predicts the type of Skin Disease and provide the result as a possibility. It acts as a one stop solution where people can find the result without waiting in long queue for the result and it also has extended features where you can interact with doctors with any delay and can find solutions to be cured before any fatality happens.<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
    st.write(" ")
    result = st.button ("Video Calling")
    if result:
        import streamlit.components.v1 as components
       components.html(
    """
    <head>
  <script src='https://meet.jit.si/external_api.js'></script>
</head>
<body>
 
<button id="start" type="button">Start</button>
<div id="jitsi-container">
</div>
 
<script>
var button = document.querySelector('#start');
var container = document.querySelector('#jitsi-container');
var api = null;
 
button.addEventListener('click', () => {
    var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var stringLength = 30;
 
    function pickRandom() {
    return possible[Math.floor(Math.random() * possible.length)];
    }
 
var randomString = Array.apply(null, Array(stringLength)).map(pickRandom).join('');
 
    var domain = "meet.jit.si";
    var options = {
        "roomName": randomString,
        "parentNode": container,
        "width": 600,
        "height": 600,
    };
    api = new JitsiMeetExternalAPI(domain, options);
});
 
</script>
</body>
</html>
""",
    height=600
)   
    new_title = '<p style="font-family:Sans One; color:Red; font-size: 32px;"><b>Contact:<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Sans One; color:Red; font-size: 32px;"><b>Joel John Joseph:<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Sans One; color:Red; font-size: 32px;"><b>joeljoseph1810@gmail.com:<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
   
