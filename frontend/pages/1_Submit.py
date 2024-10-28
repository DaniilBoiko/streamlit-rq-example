import os
import streamlit as st
import redis
from rq import Queue


def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


param = st.text_input("Enter the parameter")

if st.button("Submit"):
    st.write("Submitting the long request")

    redis_url = os.environ.get('REDIS_HOST')
    conn = redis.from_url(redis_url)

    q = Queue(connection=conn)
    job = q.enqueue("worker.submit_request", param)
    job.meta['status'] = 'Submitted'
    job.save_meta()

    st.write("Redirecting to the results page")
    nav_to(f"/Results?job_id={job.id}")
