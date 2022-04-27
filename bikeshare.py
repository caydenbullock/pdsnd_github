import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Would you like to see data for Chicagox, New York City, or Washington?: \n").lower()
        if city == "chicago":
            break
        if city == "new york city":
            break
        if city == "washington":
            break
        else: print("You must supply a valid input identical to one of the following without quotations:\n 'Chicago', 'New York City', or 'Washington'")

        # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Would you like data for 'all' months, or 'january', 'february', 'march', 'april', or 'june'?: \n").lower()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter a specific day of the week, or 'all' if no filter is desired.\n").title()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df["Start Time"].dt.day_name


    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['weekday'] == day]

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()
    print("The most popular month of bikeshare use is: ", popular_month)

    # TO DO: display the most common day of week
    popular_dow = df['day of week'].mode[0]
    print("The most popular day of week for bikeshare use is: ", popular_dow)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()
    print("The most popular starting hour for bikeshare use is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most popular starting station: ", df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print("The most popular end station: ", df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
    print("End + Start Station Combo: ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total time travelled: ', sum(df['End Time'] - df['Start Time']))


    # TO DO: display mean travel time
    print('average time travelled: ', (df['End Time'] - df['Start Time']).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
