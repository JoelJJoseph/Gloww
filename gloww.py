import streamlit as st
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
       st.components.v1.html(
"""<head>
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
</html>"""
,
    height=600
)   
    new_title = '<p style="font-family:Sans One; color:Red; font-size: 32px;"><b>Contact:<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.write(" ")
    st.components.v1.html(
    """
   <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'><link rel="stylesheet" href="./style.css">

<ul>
    <li><a href="https://twitter.com/Deathstroke1810" target="_blank"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
  <li><a href="https://github.com/JoelJJoseph" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a></li>
  <li><a href="https://www.linkedin.com/in/captain-bruce-2b77a41a4/" target="_blank"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
 </ul><style>body {
  margin: 0;
  padding: 0;
  background: #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

@media (max-width: 600px) {
  ul {
    transform: scale(0.6);
  }
}

@media (min-width: 601px) and (max-width: 700px) {
  ul {
    transform: scale(0.7);
  }
}

@media (min-width: 701px) and (max-width: 800px) {
  ul {
    transform: scale(0.8);
  }
}

ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
}

ul li {
  margin: 0 40px;
}

ul li a .fa {
  font-size: 40px;
  color: #555;
  line-height: 80px;
  transition: 0.5s;
}

ul li a {
  position: relative;
  display: block;
  width: 80px;
  height: 80px;
  background: #fff;
  text-align: center;
  transform: perspective(1000px) rotate(-30deg) skew(25deg) translate(0,0);
  transition: 0.5s;
  box-shadow: -20px 20px 10px rgba(0, 0, 0, 0.5);
}

ul li a::before {
  content: "";
  position: absolute;
  top: 10px;
  left: -20px;
  height: 100%;
  width: 20px;
  background: #b2b2b2;
  transition: 0.5s;
  transform: rotate(0deg) skewY(-45deg);
}

ul li a::after {
  content: "";
  position: absolute;
  bottom: -20px;
  left: -10px;
  height: 20px;
  width: 100%;
  background: #e5e5e5;
  transition: 0.5s;
  transform: rotate(0deg) skewX(-45deg);
}

ul li a:hover {
  transform: perspective(1000px) rotate(-30deg) skew(25deg) translate(20px,-20px);
  box-shadow: -50px 50px 50px rgba(0, 0, 0, 0.5);
}

ul li:hover .fa {
  color: #fff;
}

ul li:hover:nth-child(1) a {
  background-color: #66b4ef;
}

ul li:hover:nth-child(1) a::before {
  background-color: #66b4ef;
}

ul li:hover:nth-child(1) a::after {
  background-color: #66b4ef;
}

ul li:hover:nth-child(2) a {
  background-color: black;
}

ul li:hover:nth-child(2) a::before {
  background-color: black;
}

ul li:hover:nth-child(2) a::after {
  background-color: black;
}

ul li:hover:nth-child(3) a {
  background-color: #0e76a8;
}

ul li:hover:nth-child(3) a::before {
  background-color: #0e76a8;
}

ul li:hover:nth-child(3) a::after {
  background-color:#0e76a8;
  <link>https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css</link>
}
</style>""")



