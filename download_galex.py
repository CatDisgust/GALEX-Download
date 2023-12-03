from astroquery.mast import Observations
import os
import sys
from astropy.coordinates import SkyCoord
import astropy.units as u

def search_and_download_galex_data(coordinate, radius, download_path):
    try:
        sky_coord = SkyCoord(coordinate, unit=(u.deg, u.deg), frame='icrs')

        # 查询指定区域的观测数据
        obs_table = Observations.query_region(sky_coord, radius=radius)

        print(f"Found {len(obs_table)} observations.")

        if len(obs_table) > 0:
            galex_obs = obs_table[obs_table['obs_collection'] == 'GALEX']

            if len(galex_obs) > 0:
                data_products = Observations.get_product_list(galex_obs)

                # 过滤NUV和FUV数据产品
                nuv_fuv_products = data_products[
                    [any(substring in str(product['description']).upper() for substring in ['NUV', 'FUV'])
                     for product in data_products]
                ]

                if len(nuv_fuv_products) > 0:
                    # 下载数据产品
                    download_info = Observations.download_products(nuv_fuv_products,
                                                                   download_dir=download_path)
                    print(f"Downloaded NUV and FUV data to {download_path}")
                else:
                    print("No suitable NUV or FUV data products found.")
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
