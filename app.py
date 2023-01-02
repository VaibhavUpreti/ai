import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('model.sav', 'rb'))

st.set_page_config(page_title="Basketball Player Salary", page_icon="🏀")
st.title('Basketball Player Salary Prediction')
st.sidebar.header('Data')
image = Image.open('bb.jpg')
st.image(image, '')

st.markdown('A simple webapp that predicts net worth of basketball players in a season based on: rating and past performances')

based_on = ['Rating - rating of the player', 'Jersey Number - which signifies level of player', 'Team - teams that have won previous championships tend to pay more',
            'Playing Position - point guards are usually most paid', 'Country - country of the player', 'Draft Year - accounts inflation', 'Draft Peak']


s2 = ''
for i in based_on:
  s2 += "- " + i + "\n"
st.markdown(s2)


all_teams = [
'Atlanta Hawks',
'Boston Celtics',
'Brooklyn Nets',
'Charlotte Hornets',
'Chicago Bulls',
'Cleveland Cavaliers',
'Dallas Mavericks',
'Denver Nuggets',
'Detroit Pistons',
'Golden State Warriors',
'Houston Rockets',
'Indiana Pacers',
'Los Angeles Clippers',
'Los Angeles Lakers',
'Memphis Grizzlies',
'Miami Heat',
'Milwaukee Bucks',
'Minnesota Timberwolves',
'New Orleans Pelicans',
'New York Knicks',
'Oklahoma City Thunder',
'Orlando Magic',
'Philadelphia 76ers',
'Phoenix Suns',
'Portland Trail Blazers',
'Sacramento Kings',
'San Antonio Spurs',
'Toronto Raptors',
'Utah Jazz',
'Washington Wizards']

s1 = ''
z = 1


# FUNCTION
def user_report():


  rating = st.sidebar.slider('Rating', 50,100, 1 )
  jersey = st.sidebar.slider('Jersey Number', 0,100, 1 )
  #set_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
  team = st.sidebar.slider('Team', 0,30, 1 )
 #  position = st.sidebar.selectbox('Position', ('C', 'G', 'F-C','F-G','G-F'))
  position = st.sidebar.slider('Position', 0,10, 1 )
  #country = st.sidebar.select_slider('Country', options=['USA', 'AUS', 'CAD']
   # )
  country = st.sidebar.radio(
    "Set Country: 1-USA, 2-AUS, 3-CAD ",
    key="visibility",
    options=[1, 2,3],
    )
  # 0,3, 1 )
  draft_year = st.sidebar.slider('Draft Year', 2000,2020, 2000)
  draft_round = st.sidebar.slider('Draft Round', 1,10, 1)
  draft_peak = st.sidebar.slider('Draft Peak', 1,30, 1)

  user_report_data = {
      'rating':rating,
      'jersey':jersey,
      'team':team,
      'position':position,
      'country':country,
      'draft_year':draft_year,
      'draft_round':draft_round,
      'draft_peak':draft_peak
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Player Data')
st.write(user_data)


salary = model.predict(user_data)
st.subheader('Predicted Salary for the League')
sal = np.round(salary[0], 2)

st.subheader('💵 ' + "{:,}".format(sal) + ' USD')


st.header('All NBA Teams: ')
for i in all_teams:
  #s1 += "- " + i  + str(z) + '\n'
  s1 += str(z) + "." + i + "\n \n"
  z+=1
st.markdown(s1)

#st.subheader('💵' + str(np.round(salary[0], 2)) + ' USD')
st.header('Contributors:')

contributors = ['Drishti Seth', 'Shivesh Ranjan', 'Vaibhav Upreti']

s = ''
for i in contributors:
  s += "- " + i + "\n"
st.markdown(s)
