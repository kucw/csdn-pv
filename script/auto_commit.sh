#!/bin/bash

cur_date="`date +%Y-%m-%d`" 
commit_msg="auto update data "${cur_date}
git add ..
git commit -m "${commit_msg}"
