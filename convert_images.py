# Set the input path

input_path = './datasets/images/*.jpg'

# Read the image and convert it to the numpy array

for img_path in glob.glob(input_path):
    try:
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        basename = os.path.basename(img_path)
        output_path = f'./data/Synapse/test_vol_h5/{os.path.splitext(basename)[0]}.npz'
        np.savez(output_path, img)
        print(f'Saved {output_path}')
    except Exception as e:
        print(f"Failed to read image {img_path}: {e}")
