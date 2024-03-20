import fiftyone as fo

import fiftyone.zoo as foz

# The path to the source files that you manually downloaded
name = "hitl_damages"
data_path = "../data/humansintheloop/Car parts dataset/File1/img"
labels_path = "../data/humansinhteloop/Car parts dataset/ann"

# The type of the dataset being imported
dataset_type = fo.types.COCODetectionDataset  # for example

dataset = fo.Dataset.from_dir(
    data_path=data_path, labels_path=labels_path, dataset_type=dataset_type
)

if __name__ == "__main__":
    # Ensures that the App processes are safely launched on Windows
    session = fo.launch_app(dataset=dataset, desktop=True)
    session.wait()
