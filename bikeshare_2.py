import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days= ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city= " "
    while city not  in CITY_DATA.keys():
        city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
        if city in CITY_DATA.keys():
            city=city
            break
        else:
             print("sorry name of city not found! Please try again ...")

    filter1=" "

    while filter1 !="month" or filter1 !="day" or filter1 !="all":
        filter1=input("Would you like to filter the data by 'month', 'day', or 'all' for no filter date?")

        if filter1=="month":
           month=input("Which month - January, February, March, April, May, or June?").lower()
           if month not in months:
              print("sorry name of month not match! Please try again ...")
           else:
            day="all"
            break

        elif filter1=="day":
           day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()
           if day not in days:
                print("sorry name of day not match! Please try again ...")
           else:
             month="all"
             break
        elif filter1=="all":
           month="all"
           day="all"
           break

        else:
                print ("Please try again to filter data by 'month', 'day', or 'all' for no filter date")


    print('-'*40)
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]-1

    print('Most Popular Month:', months[popular_month])

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day Of Week:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print("Most Commonly Used Start Station: ",start_station)

    # display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print("Most Commonly Used End Station",end_station)

    # display most frequent combination of start station and end station trip
    frequent_trip =(df['Start Station']+" "+df['End Station']).mode()[0]
    print("Most Frequent Combination Of Start Station And End Station Trip",frequent_trip)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df['Trip Duration'].sum()
    print("Total Travel Time: ",total_time)


    # display mean travel time
    mean_time=df['Trip Duration'].mean()
    print("mean travel time: ",mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent=df['Birth Year'].max()
        print("Most Recent Birth Years: ", most_recent)

        earliest=df['Birth Year'].min()
        print("Earliest Birth Yeears: ",earliest)

        most_common_year=df['Birth Year'].mode()[0]
        print("Most Common Year Of Birth: ",most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data on user ask."""
    count = 0
    while True:
        #Display five row data if user want
        raw_data = input('Would you like to see 5 lines of raw data? Enter yes or no.')
        if raw_data.lower() == 'yes':
            print(df.iloc[count:count+5])
            count = count + 5
        else:
            break
def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #send df verable for all method
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        # ask user if the want restart program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
