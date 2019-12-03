import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # cities = ['washington', 'new york city', 'chicago']

    while True:
        try:
            city = input('\nwould you like to see data for Chicago, New York, or Washington?: ').lower()
            if city in CITY_DATA:
                print('good')
                break
            elif city not in CITY_DATA:
                print('wrong city value. please retry')
        except:
            pass

    while True:
        try:
            month = input(
                '\nwhat month would you like to filter by? Please enter month in full; otherwise enter "all": ').lower()
            if month in months:
                print('Thank you for your input')
                break
            elif month not in months:
                print('\nwrong month value. try again\n')
        except:
            pass

    while True:
        try:
            day = input(
                '\nwhat day in week would you like to filter by? please enter day in full. otherwise enter "all": ').lower()
            if day in days:
                print('good')
                break
            elif day not in days:
                print('\nwrong day value. try again\n')
        except:
            pass

    print('-' * 40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding integer
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]  # title() method to enable first letter a CAPITAL letter

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # popular_month = df['month'].mode()[0]
    # popular_month = popular_month - 1
    # print('Most popular month for travelling is: ', popular_month)
    # months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('tweede print', df.head())
    print('The most common month is: ', months[df['month'].mode()[0]].title())

    # TO DO: display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print('Most popular day-of-week for travelling is: ', popular_dayofweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour for travelling is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used Start Station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used Start Station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_trip = df['Start End'].value_counts().idxmax()  # idxmax = take row label with the maximum value
    print('Most common trip between Start Station & End Station is: ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total time of travel is {} seconds '.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean time of travel is {} seconds'.format(int(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of User Types
    print('The count per User Type is: ', df['User Type'].value_counts().to_frame())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nThe count of travellers per Gender is: ', df['Gender'].value_counts().to_frame())
    else:
        df['Gender'] = np.nan
        print('\nGender column is missing in dataset of this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The earliest year of birth is: ', int(df['Birth Year'].min()))
        print('\nThe most recent year of birth is: ', int(df['Birth Year'].max()))
        print('\nThe most common year of birth is: ', int(df['Birth Year'].mode()[0]))
    else:
        df['Birth Year'] = np.nan
        print('\nThe Birth Year column is missing in dataset of this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# get user input for data displaying successive five rows of data at a time
def display_data(df):
    while True:
        i = 0
        j = 5
        dat = input('Would you like to view the data? Enter "yes" or "no".\n')
        if dat.lower() == 'y' or dat.lower() == 'yes':
            df = df.iloc[i:j]
            print('These are the first five rows of the data\n', df)
            i += 1
            j += 1
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
