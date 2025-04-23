import pandas as pd
import itertools

data = {
    'date': ['2024-01-15', '2024-01-20', '2024-02-10', '2024-01-25'],
    'artist': ['Taylor', 'Drake', 'Taylor', 'Taylor'],
    'venue': ['MSG', 'MSG', 'MSG', 'O2 Arena']
}
concerts = pd.DataFrame(data)
concerts['date'] = pd.to_datetime(concerts['date'])
concerts['year_month'] = concerts['date'].dt.to_period('M')
all_artists = ['Taylor', 'Drake']
all_venues = ['MSG', 'O2 Arena']
artist_venue_comb = list(itertools.product(all_artists, all_venues))
grouped_data = concerts.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')
wide_df = grouped_data.pivot_table(
    index='year_month',
    columns=['artist', 'venue'],
    values='count',
    fill_value=0  
)
wide_df = wide_df.reindex(columns=pd.MultiIndex.from_tuples(artist_venue_comb), fill_value=0)
wide_df.columns = [f"{artist}_{venue}" for artist, venue in wide_df.columns]
wide_df = wide_df.reset_index()
wide_df['year_month'] = wide_df['year_month'].astype(str)
print(wide_df)