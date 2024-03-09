from typing import List

hyphen_e = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        for req in file_obj.readlines():
            req = req.strip()
            if req != hyphen_e:
                requirements.append(req)

    return requirements