from astroquery.mast import Observations
import os
import sys
from astropy.coordinates import SkyCoord
import astropy.units as u

def search_and_download_galex_data(coordinate, radius, download_path):
    try:
        sky_coord = SkyCoord(coordinate, unit=(u.deg, u.deg), frame='icrs')

        obs_table = Observations.query_region(sky_coord, radius=radius)

        print(f"Found {len(obs_table)} observations.")

        if len(obs_table) > 0:
            galex_obs = obs_table[obs_table['obs_collection'] == 'GALEX']

            if len(galex_obs) > 0:
                data_products = Observations.get_product_list(galex_obs)

                # 打印出找到的数据产品信息
                print("Available data products:")
                print(data_products)

                # 筛选出数据产品
                filtered_products = Observations.filter_products(data_products)

                if len(filtered_products) > 0:
                    download_info = Observations.download_products(filtered_products,
                                                                   download_dir=download_path)
                    print(f"Downloaded data to {download_path}")
                else:
                    print("No suitable data products found.")
            else:
                print("No GALEX observations found within the specified region.")
        else:
            print("No observations found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python download_galex.py <coordinate> <radius> <download_path>")
        sys.exit(1)

    coordinate = sys.argv[1]
    radius = sys.argv[2]
    download_path = sys.argv[3]

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    search_and_download_galex_data(coordinate, radius, download_path)

if __name__ == "__main__":
    main()
