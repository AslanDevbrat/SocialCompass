try:
    import torch
    import imagebind
    import pandas as pd
    import numpy as np
    import sklearn

    print("🎉 恭喜！你的'电脑厨房'一切就绪！")
    print(f"    - PyTorch (引擎) 版本: {torch.__version__}")
    print("    - ImageBind (大厨) 已就位!")
    print(f"    - Pandas (食材处理工具) 版本: {pd.__version__}")
    print("\n现在你可以开始准备'食材' (数据集) 了！")

except ImportError as e:
    print(f"😭 出了一点小问题: {e}")
    print("有名厨具没有安装好，请检查一下第二步的安装命令是否都成功运行了。")