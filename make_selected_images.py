import pandas as pd
import os

data_dir = "data"
def main():
    # Load base dataset
    df = pd.read_csv(os.path.join(data_dir,'base_dataset.csv'))

    # Sort images by prompt length (ascending for progressive difficulty)
    df_sorted = df.sort_values(by='prompt_length', ascending=True)

    # Create level assignments (10 images per level, increasing difficulty)
    df_sorted['level'] = (df_sorted.index // 10) + 1  # 3 levels total

    df_sorted['image_number'] = df_sorted.groupby('level').cumcount() + 1

    # Mark daily challenge images (hardest in each level)
    df_sorted['type'] = 'regular'
    daily_indices = df_sorted.groupby('level').tail(1).index
    df_sorted.loc[daily_indices, 'type'] = 'daily'

    # Format for game server
    df_selected = df_sorted.rename(columns={
        'image_name': 'id',
        'prompt': 'prompt'
    })[['id', 'prompt', 'level', 'image_number', 'type']].copy()

    # Add image URLs (assuming images stored in data/selected_images/)
    df_selected['image_url'] = '/data/selected_images/' + df_selected['id']

    # Save to CSV
    df_selected.to_csv('selected_images.csv', index=False)

    print("Generated selected_images.csv with:")
    print(f"- {df_selected['level'].max()} levels")
    print(f"- {len(df_selected)} total images")
    print(f"- {len(df_selected[df_selected['type']=='daily'])} daily challenges")


if __name__ == "__main__":
    main()