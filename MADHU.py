import streamlit as st

st.title("THIS MIGHT SCARE YOU.")
st.subheader("BEWARE")

st.header("M.A.D.H.U")
st.text("Code name for Mad, Astonishing, Devil, Hologram, from, Uber eats")

col1, col2 = st.columns(2)

with col1:
    st.header('MAD')
    content = """
    Mad is the first word in M.A.D.H.U.
    It implies that this beast is angry.
    It also implies that this beast is crazy.
    So BEWARE...
    """
    st.write(content)
    st.header('DEVIL')
    content1 = """
        Devil is the third word in M.A.D.H.U.
        It implies that this beast is a devil.
        It also implies that this beast is evil.
        So BEWARE...
        """
    st.write(content1)

with col2:
    st.header('ASTONISHING')
    content2 = """
    Astonishing is the second word in M.A.D.H.U.
    It implies that humanity is surprised this beast exists.
    It doesn't implie that the beast is amazing in any sort (unless you count amazingly evil).
    So BEWARE...
    """
    st.write(content2)
    st.header('HOLOGRAM')
    content3 = """
        Hologram is the fourth word in M.A.D.H.U.
        It implies that this beast is a hologram.
        It also implies that this beast is indestructible.
        So BEWARE...
        """
    st.write(content3)

st.title("FROM UBER EATS")
content4 = """
from uber eats are the last words in M.A.D.H.U.
It implies that uber eats made the beast.
It also implies that uber eats is evil.
So BEWARE...
"""

st.write(content4)

st.title("I hope everyone reading this lives...")
st.header("Good Luck fellow humans.")
st.subheader("Unless you are M.A.D.H.U.")
st.text("Also Good Luck extraterrestrials!")
