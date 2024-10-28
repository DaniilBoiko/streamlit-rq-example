import os
import time

import streamlit as st
import redis
from rq import Queue


def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


if 'job_id' not in st.query_params:
    st.switch_page("pages/1_Submit.py")

redis_url = os.environ.get('REDIS_HOST')
conn = redis.from_url(redis_url)

q = Queue(connection=conn)

job_id = st.query_params['job_id']
job = q.fetch_job(job_id)

if job.meta['status'] == 'Completed':
    st.write(f"Results for {job.result}")
else:
    st.write(f"Status: {job.meta['status']}")
    st.write("Refreshing the page in one second")
    st.write("Please wait...")
    time.sleep(1)
    st.rerun()
