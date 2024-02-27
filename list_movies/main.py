import requests
from bs4 import BeautifulSoup

def extract_text_by_class(url, class_name, output_file):
    page_number = 1  # Starting page number
    while True:
        # Create the URL with the current page number
        page_url = f"{url}/?get-page={page_number}"
        
        # Send an HTTP GET request to the page URL
        response = requests.get(page_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all elements with the specified class
            elements_with_class = soup.find_all(class_=class_name)
            
            # If no elements are found, break the loop
            if not elements_with_class:
                break
            
            # Open the output file in write mode
            with open(output_file, 'a', encoding='utf-8') as file:
                # Extract and write the text from each element to the file
                for element in elements_with_class:
                    file.write('['+str(page_number)+']'+element.get_text() + '\n')
            
            # Increment the page number for the next iteration
            page_number += 1
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            break

if __name__ == "__main__":
    target_url = "https://isaidub3.co/movie/tamil-dubbed-movies-download"  # Replace this with the base URL
    target_class = "f"  # Replace this with the actual class name
    output_file = "isaidub3.co.txt"  # Name of the output text file
    
    extract_text_by_class(target_url, target_class, output_file)
