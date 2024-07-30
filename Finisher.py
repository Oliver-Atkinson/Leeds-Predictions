import smtplib
from email.message import EmailMessage
import shutil
import pandas as pd
import numpy as np

# if '−' == '-': print('yup')
# else: print('nope')
# exit()

fixs_df = pd.read_table("Fixtures.dat", dtype = {'Date': str, 'Time': str, 'Result': str}, sep=' ')
fix_list = fixs_df['Team'].tolist()
fix_list = [fix.replace("_", " " ) for fix in fix_list]
ven_list = fixs_df['H/A'].tolist()
fix_list = [fix_list[i]+' ('+ven_list[i]+')' for i in range(len(fix_list))]
res_list = fixs_df['Result'].tolist() 
n_res = res_list.index(np.nan)

outputs = ['Matrix.pdf', 'Rankings.pdf', 'LinePoints.pdf', 'LineScores.pdf', 'race.mp4', 'Summary.pdf', 'ItrGamMatrix.pdf']

dest_dir = '//Users/oliver/Documents/Drive/LeedsPreds/'
dad_dir = 'Dads/Dad'
for out in outputs:
    shutil.copyfile(out, dest_dir+out)
    shutil.copyfile(dad_dir+out, dest_dir+'Dad'+out)

shutil.copyfile('Champ_pointspos_NoDeds.pdf', dest_dir+'Champ_pointspos_NoDeds.pdf')
shutil.copyfile('Boxplot.pdf', dest_dir+'Boxplot.pdf')

# set your email and password
# please use App Password
email_address = "greggpsikas279@gmail.com"
email_password = "elhgvxqvemjedyxe"

# create email
msg = EmailMessage()
msg['Subject'] = "Leeds Predictions"
msg['From'] = email_address
msg['To'] = "oliveratkinson0907@gmail.com"
msg.set_content("Computations for today's game - "+fix_list[n_res-1]+", "+res_list[n_res-1][0]+'-'+res_list[n_res-1][1]+" - have been completed and a full set of outputs moved to Google Drive.")

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)