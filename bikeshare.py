import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#city, month, day = 'new_york_city', 'January', 'Monday'


def get_filters():
    city = input("Which city do you want to analyze? Pick one of the following: 'chicago', 'NYC', 'washington' ")
    while city not in ('chicago', 'NYC', 'washington'):
        city = input("Oops! Seems like you misspelled the city you want to look at. Please pick one of the following: 'chicago', 'NYC', 'washington' ")
    month = input("Which month would you like to analyze? Pick one of the following: 'January', 'February', 'March', 'April', 'May', 'June' or 'all' to apply no month filter")
    while month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        month = input("Oops! Seems like you misspelled the month you want to look at. Please pick one of the following: 'January', 'February', 'March', 'April', 'May', 'June' or 'all' to apply no month filter")
    day = input("Which day would you like to analyze? Pick one of the following:\n 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday' or 'all' to apply no day filter")
    while day not in ('Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all'):
        day = input("Oops! Seems like you misspelled the day you want to look at. Please pick one of the following: 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday' or 'all' to apply no day filter ")
    if month != 'all' and day != 'all':
        print("You chose to analyze data from {} collected in {} on {}.".format(city, month, day))
    if month != 'all' and day == 'all':
        print("You chose to analyze data from {}. You chose to filter it by the month '{}' and not to filter it by the day.".format(city, month))
    if month == 'all' and day != 'all':
        print("You chose to analyze data from {}. You chose to apply no filter by month and to filter it by the day '{}'.".format(city, day))
    if month == 'all' and day == 'all':
        print("You chose to analyze data from {} and not to filter it by month or day.".format(city))

    if city == 'NYC':
        city = 'new_york_city'


    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day

#city, month, day = get_filters()

# city, month, day = 'new_york_city', 'January', 'Monday'


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv('{}.csv'.format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

# print(load_data(city, month, day))


def most_common(time_unit, df):
    # city, month, day = 'new_york_city', 'January', 'Monday'
    # df = pd.read_csv('{}.csv'.format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if time_unit == 'month':
        df['month'] = df['Start Time'].dt.month
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        index = df['month'].mode()[0] - 1
        popular_time_unit = months[index]

    if time_unit == 'day of week':
        df['day'] = df['Start Time'].dt.weekday
        weekdays = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        index = df['day'].mode()[0]
        popular_time_unit = weekdays[index]

    if time_unit == 'hour':
        df['hour'] = df['Start Time'].dt.hour
        popular_time_unit = df['hour'].mode()[0]

    return ("The most common {} is ".format(time_unit) + str(popular_time_unit))



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print(most_common('month', df))

    # TO DO: display the most common day of week

    print(most_common('day of week', df))

    # TO DO: display the most common start hour

    print(most_common('hour', df))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#time_stats(pd.read_csv('{}.csv'.format(city)))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    # city, month, day = 'new_york_city', 'January', 'Monday'
    # df = pd.read_csv('{}.csv'.format(city))

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()



    # TO DO: display most commonly used start station
    x = df.groupby(['Start Station']).size()
    #print("x: ", x)
    Start_Station_aka_id = x.idxmax()
    no_of_appearances_x = x[Start_Station_aka_id]
    print("The most commonly used start station was: '{}'\n It was used {} times.".format(Start_Station_aka_id, no_of_appearances_x))


    # TO DO: display most commonly used end station

    y = df.groupby(['End Station']).size()
    #print("y: ", y)
    End_Station_aka_id = y.idxmax()
    no_of_appearances_y = y[Start_Station_aka_id]
    print("The most commonly used end station was: '{}'\n It was used {} times.".format(End_Station_aka_id, no_of_appearances_y))


    # TO DO: display most frequent combination of start station and end station trip

    z = df.groupby(['Start Station', 'End Station']).size()
    #print("z: ", z)
    Station_aka_id = z.idxmax()
    #print(Station_aka_id)
    no_of_appearances_z = z[Station_aka_id]
    print("The most frequent combination of start station (first) and end station (second) was between: {}\n This combination was used {} times.".format(Station_aka_id, no_of_appearances_z))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#station_stats(pd.read_csv('{}.csv'.format(city)))

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time_in_sec = df['Trip Duration'].sum()
    total_travel_time_in_years = total_travel_time_in_sec // (60 * 60 * 24 *365)

    modulus1_in_sec = total_travel_time_in_sec - total_travel_time_in_years*(60 * 60 * 24 *365)
    #print("modulus1_in_sec:", modulus1_in_sec)
    total_travel_time_in_months = modulus1_in_sec // (60 * 60 * 24 *31)

    modulus2_in_sec = modulus1_in_sec - total_travel_time_in_months*(60 * 60 * 24 *31)
    #print("modulus2_in_sec:", modulus2_in_sec)
    total_travel_time_in_weeks = modulus2_in_sec // (60 * 60 * 24 *7)

    modulus3_in_sec = modulus2_in_sec - total_travel_time_in_weeks*(60 * 60 * 24 *7)
    #print("modulus3_in_sec:", modulus3_in_sec)
    total_travel_time_in_days = modulus3_in_sec // (60 * 60 * 24)

    modulus4_in_sec = modulus3_in_sec - total_travel_time_in_days*(60 * 60 * 24)
    #print("modulus4_in_sec:", modulus4_in_sec)
    total_travel_time_in_hours = modulus4_in_sec // (60 * 60)

    modulus5_in_sec = modulus4_in_sec - total_travel_time_in_hours*(60 * 60)
    #print("modulus5_in_sec:", modulus5_in_sec)
    total_travel_time_in_minutes = modulus5_in_sec // 60

    modulus6_in_sec = modulus5_in_sec - total_travel_time_in_minutes*60
    #print("modulus6_in_sec:", modulus6_in_sec)
    total_travel_time_in_seconds_modulus = modulus6_in_sec

    print("total travel time of all Users combined:\n YEARS: {} \n MONTHS: {} \n WEEKS: {} \n DAYS: {} \n HOURS: {} \n MINUTES: {} \n SECONDS: {} \n".format(total_travel_time_in_years, total_travel_time_in_months, total_travel_time_in_weeks, total_travel_time_in_days, total_travel_time_in_hours, total_travel_time_in_minutes, total_travel_time_in_seconds_modulus))

    # TO DO: display mean travel time

    mean_travel_time_in_sec = df['Trip Duration'].mean()
    mean_travel_time_in_minutes = mean_travel_time_in_sec // 60
    modulus_in_sec = mean_travel_time_in_sec - mean_travel_time_in_minutes*60
    mean_travel_time_in_seconds_modulus = modulus_in_sec

    print("mean travel time:\n MINUTES: {} \n SECONDS: {} \n".format(int(mean_travel_time_in_minutes), mean_travel_time_in_seconds_modulus))

#trip_duration_stats(pd.read_csv('{}.csv'.format(city)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    x = df.groupby(['User Type']).size()
    print("printing different User Types and their counted number:\n",x)

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth


    if city in ('chicago', 'new_york_city'):
        y = df.fillna('Missing Data').groupby(['Gender']).size()
        # filling of NaN's occurs out of place, original DataFrame is NOT changes
        print("printing different genders and their counted number:\n",y)

        print("earliest birth year of a User:\n", int(df['Birth Year'].min()))
        print("most recent birth year of a User:\n", int(df['Birth Year'].max()))
        z = df.fillna('Missing Data').groupby(['Birth Year']).size()
        #print("printing z:\n", z)
        Birth_Year_aka_id = int((z.drop(['Missing Data'])).idxmax())
        print("most common birth year of Users:\n", Birth_Year_aka_id)

    else:
        print("Could not display statistics for gender counts and birth years, as this data is not available for the chosen city ({}).".format(city))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    number_of_rows = 5
    print(df.head(number_of_rows))
    repeat_loop = True
    while repeat_loop:
        more_data = input("'\nWould you like to see more raw data? You can choose the number of rows to be displayed. Enter 'yes' or 'no'.\n'")
        while more_data not in ('yes', 'no'):
            more_data = input("Oops! Seems like you misspelled your input. Please pick one of the following answers: 'yes' or 'no'")
        if more_data == 'yes':
            position_of_rows = input("'\nWould you like to see rows from the beginning or from the end of the DataFrame? Enter 'beginning' or 'end'.\n'")
            while position_of_rows not in ('beginning', 'end'):
                position_of_rows = input("Oops! Seems like you misspelled your input. Please pick one of the following answers: 'beginning' or 'end'")
            number_of_rows = int(input("'\nHow many rows (starting from the {} of the DataFrame) would you like to see? Enter an integer between 1 and 100.\n'".format(position_of_rows)))
            while number_of_rows not in (list(range(1, 101))):
                number_of_rows = int(input("Oops! Seems like you entered an invalid number of rows. Please enter an integer between 1 and 100"))
            if position_of_rows == 'beginning':
                print(df.head(number_of_rows))
            else:
                print(df.tail(number_of_rows))
        else:
            repeat_loop = False
            print("You chose not to display any further raw data.")

#show_raw_data(pd.read_csv('{}.csv'.format(city)))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data = input("\nWould you like to see the first 5 columns of raw data? Also enter 'yes' to view other raw data. Enter 'yes' or 'no'.\n")
        while raw_data not in ('yes', 'no'):
            raw_data = input("Oops! Seems like you misspelled your input. Please pick one of the following answers: 'yes' or 'no'")
        if raw_data.lower() == 'yes':
            show_raw_data(df)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
