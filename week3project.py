import requests

partner_data_unfilt = requests.get('https://ct-mock-tech-assessment.herokuapp.com/').json()
# print(partner_data_unfilt['partners'])
# for i in partner_data_unfilt['partners']:
#     if "United States" in i['country']:
#         print(i)

us_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'United States' in x['country']]
ireland_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Ireland' in x['country']]
spain_clean = [[str(x['email']) + " " + str(x['lastName']) + " " +  str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Spain' in x['country']]
mexico_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Mexico' in x['country']]
canada_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Canada' in x['country']]
singapore_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Singapore' in x['country']]
japan_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Japan' in x['country']]
uk_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'United Kingdom' in x['country']]
france_clean = [[str(x['email']) + " " + str(x['lastName']) + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'France' in x['country']]
# print(canada_clean)

clean_dict = {
    'United States': us_clean,
    'Ireland': ireland_clean,
    'Spain': spain_clean,
    'Mexico': mexico_clean,
    'Canada': canada_clean,
    'Singapore': singapore_clean,
    'Japan': japan_clean,
    'United Kingdom': uk_clean,
    'France': france_clean
}

# def fill_meeting(country, dict):
#     dict['attendee_count'] += 1
#     dict['attendees'] = [x['email'] for x in clean_dict[country]]

# Function to return the desired format of the meetings. WORK ON THIS TOMORROW
def create_meet(country):
    meetings = {
        'location': country,
        'start_date': '',
        'attendee_count': 0,
        }
    start_april = '2017-04-25'
    end_april = '2017-04-28'
    start_may = '2017-05-03'
    end_may = '2017-05-22'
    start_june = '2017-06-02'
    end_june = '2017-06-08'
    for i in country:
        if '2017-06-01' and '2017-06-02' and '2017-06-03' in i:
            # fill_meeting(country, meetings)
            meetings['start_date'] = start_june
        elif '2017-06-07' and '2017-06-08' and '2017-06-09' in i:
            # fill_meeting(country, meetings)
            meetings['start_date'] = end_june

    
    return meetings
print(create_meet(us_clean))

