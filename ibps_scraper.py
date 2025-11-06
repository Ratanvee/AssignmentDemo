import pandas as pd
from datetime import datetime

def scrape_ibps_jobs():
    """
    Creates sample IBPS job listings for demonstration
    Returns a list of dictionaries containing job information
    """
    try:
        # Sample job listings data for demonstration
        # In a real-world scenario, this would be scraped from the IBPS website
        mock_data = [
            {
                'Job Title': 'Recruitment of Probationary Officers/Management Trainees',
                'Location': 'Pan India',
                'Post Date': '01/11/2025',
                'Job Link': 'https://www.ibps.in/po-mt-notification-2025/'
            },
            {
                'Job Title': 'Recruitment of Clerks in Participating Banks',
                'Location': 'Pan India',
                'Post Date': '15/10/2025',
                'Job Link': 'https://www.ibps.in/clerk-notification-2025/'
            },
            {
                'Job Title': 'Specialist Officers in Participating Banks',
                'Location': 'Pan India',
                'Post Date': '20/10/2025',
                'Job Link': 'https://www.ibps.in/so-notification-2025/'
            }
        ]
        
        # Create DataFrame from data
        df = pd.DataFrame(mock_data)
        
        # Save to CSV with current date
        filename = f'ibps_jobs_{datetime.now().strftime("%Y%m%d")}.csv'
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Job listings saved to {filename}")
        print(f"Found {len(mock_data)} job listings")
        
        return mock_data
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    scrape_ibps_jobs()