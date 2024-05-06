import streamlit as st

def calculate_hints(head_impulse, nystagmus, test_of_skew):
    if head_impulse == 'Normal' and nystagmus == 'Direction-changing' and test_of_skew == 'Present':
        return 'Central'
    else:
        return 'Peripheral'

def main():
    st.title('HINTS for Stroke in Acute Vestibular Syndrome Calculator')
    st.write('Enter the findings from the HINTS examination to determine the likelihood of stroke in patients with acute vestibular syndrome.')

    head_impulse = st.selectbox('Head Impulse Test:', ['Normal', 'Abnormal'])
    nystagmus = st.selectbox('Nystagmus:', ['Direction-changing', 'Unidirectional'])
    test_of_skew = st.selectbox('Test of Skew:', ['Present', 'Absent'])

    if st.button('Calculate HINTS Result'):
        hints_result = calculate_hints(head_impulse, nystagmus, test_of_skew)
        st.write(f'HINTS Result: {hints_result}')

if __name__ == '__main__':
    main()
