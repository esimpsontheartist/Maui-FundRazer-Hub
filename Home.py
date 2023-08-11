# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='Maui Fundrazer Art Charity Project Hub', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Maui Fundrazer Art Charity Project Hub')

# Content
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = st.columns(14)
c1.image(Image.open('images/ethereum-logo.png'))
c2.image(Image.open('images/bsc-logo.png'))
c3.image(Image.open('images/polygon-logo.png'))
c4.image(Image.open('images/solana-logo.png'))
c5.image(Image.open('images/avalanche-logo.png'))
c6.image(Image.open('images/cosmos-logo.png'))
c7.image(Image.open('images/near-logo.png'))
c8.image(Image.open('images/flow-logo.png'))
c9.image(Image.open('images/thorchain-logo.png'))
c10.image(Image.open('images/osmosis-logo.png'))
c11.image(Image.open('images/gnosis-logo.png'))
c12.image(Image.open('images/optimism-logo.png'))
c13.image(Image.open('images/arbitrum-logo.png'))
c14.image(Image.open('images/axelar-logo.png'))

st.write(
    """
    Maui Fundrazer Tools for Users is here for your viewing needs and pleasure.

 * PUT sales COPY HERE for public later *
    """
)


st.subheader('Future Works')
st.write(
    """
Roadmap data here.
    """
)
