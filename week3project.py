import statistics
import requests

partner_data_unfilt = requests.get('https://ct-mock-tech-assessment.herokuapp.com/').json()

cleaned_dict = {
    'United States': { 'Partners': [x for x in partner_data_unfilt['partners'] if 'United States' in x['country']]},
    'Ireland': {'Partners': [x for x in partner_data_unfilt['partners'] if 'Ireland' in x['country']]},
    'Spain': {'Partners': [x for x in partner_data_unfilt['partners'] if 'Spain' in x['country']]},
    'Mexico': {'Partners': [x for x in partner_data_unfilt['partners'] if 'Mexico' in x['country']]},
    'Canada': {'Partners': [x for x in partner_data_unfilt['partners'] if 'Canada' in x['country']]},
    'Singapore': {'Partners': [x for x in partner_data_unfilt['partners'] if 'Singapore' in x['country']]},
    'Japan': {'Partners': [x for x in partner_data_unfilt['partners'] if 'Japan' in x['country']]},
    'United Kingdom': {'Partners': [x for x in partner_data_unfilt['partners'] if 'United Kingdom' in x['country']]},
    'France': {'Partners': [x for x in partner_data_unfilt['partners'] if 'France' in x['country']]}  
}

# Function for returning the newly formatted api with the start dates, attendees, and the attendee count
def create_meeting(a_dict):
    dates = []
    attendees = []
    current_country = ''
    attendees_count = 0
    meetings_for_partners_by_country = []
    for i in a_dict:
        current_country = i
        for partner in a_dict[i]['Partners']:
            for date in partner['availableDates']:
                dates.append(date)
            if statistics.mode(dates) in partner['availableDates']:
                attendees.append(partner['lastName'])
                attendees_count += 1

            meetings = {
                'location': current_country,
                'start_date': statistics.mode(dates),
                'attendee_count': attendees_count,
                'attendees': attendees,
                }
        meetings_for_partners_by_country.append(meetings)
    return meetings_for_partners_by_country
print(create_meeting(cleaned_dict))

# post_data = create_meeting(cleaned_dict)

# p = requests.post('https://ct-mock-tech-assessment.herokuapp.com/', data=post_data)

