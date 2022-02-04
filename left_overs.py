
# clean_dict = {
#     'United States': [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'United States' in x['country']],
#     'Ireland': [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Ireland' in x['country']],
#     'Spain': [[str(x['email']) + " " + str(x['lastName']) + " " +  str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Spain' in x['country']],
#     'Mexico':  [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Mexico' in x['country']],
#     'Canada': [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Canada' in x['country']],
#     'Singapore': [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Singapore' in x['country']],
#     'Japan': [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'Japan' in x['country']],
#     'United Kingdom': [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'United Kingdom' in x['country']],
#     'France': [[str(x['email']) + " " + str(x['lastName']) + " " + str(x['availableDates'])] for x in partner_data_unfilt['partners'] if 'France' in x['country']]
# }

# print(clean_dict['United States'])
# def fill_meeting(country, dict):
#     dict['attendee_count'] += 1
#     dict['attendees'] = [x['email'] for x in clean_dict[country]]

# Function to return the desired format of the meetings. WORK ON THIS TOMORROW
def create_meet(a_dict):
    # start_april = '2017-04-25'
    # end_april = '2017-04-28'
    # start_may = '2017-05-03'
    # end_may = '2017-05-22'
    # start_june = '2017-06-02'
    # end_june = '2017-06-08'
    current_country = ''
    for i in a_dict:
        current_country = i
        meetings = {
            'location': current_country,
            'start_date': '',
            'attendee_count': 0,
            }

    # for i in country:
    #     if '2017-06-01' and '2017-06-02' and '2017-06-03' in i:
    #         # fill_meeting(country, meetings)
    #         meetings['start_date'] = start_june
    #     elif '2017-06-07' and '2017-06-08' and '2017-06-09' in i:
    #         # fill_meeting(country, meetings)
    #         meetings['start_date'] = end_june

    
    return meetings
# print(create_meet(clean_dict))

