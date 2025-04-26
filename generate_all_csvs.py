from ktc_scraper import scrape_ktc, export_to_csv

def run_all_scrapes():
    players = scrape_ktc(scrape_redraft=False)

    # 1QB, No TEP
    export_to_csv(players, format='1QB', tep=0, filename='ktc_1qb.csv')

    # 1QB, TEP
    export_to_csv(players, format='1QB', tep=1, filename='ktc_1qb_tep.csv')

    # Superflex, No TEP
    export_to_csv(players, format='SF', tep=0, filename='ktc_sf.csv')

    # Superflex, TEP
    export_to_csv(players, format='SF', tep=1, filename='ktc_sf_tep.csv')

if __name__ == "__main__":
    run_all_scrapes()
