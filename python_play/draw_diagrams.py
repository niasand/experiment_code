# @Author: Zhiwei Yang
# @Date:   2021/1/24
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from util_tools.file_utils import return_absoulte_path_from_home

save_file_path = return_absoulte_path_from_home("Desktop")


def drwa_example():
    with Diagram("web_service", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")
