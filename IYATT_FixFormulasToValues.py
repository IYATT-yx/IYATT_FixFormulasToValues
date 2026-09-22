'''
file: IYATT_FixFormulasToValues.py
description: 将选中区域内的公式批量转换为静态值
author: IYATT-yx
copyright:   Copyright (c) 2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
'''
from pytableenginesdk import utils

pluginInfo = {
    'name': 'FixFormulasToValues',
    'author': 'IYATT',
    'description': '将选中区域的公式固定为静态值',
    'version': '0.0.1',
}

def _processFixValues(appComHandle, targets, logger):
    totalAreas = 0
    for sheetName, address, mainRng in targets:
        logger.info(f'正在处理工作表 [{sheetName}] 的区域 [{address}]...')
        for subRng in utils.forEachArea(mainRng):
            subRng.Value = subRng.Value
            totalAreas += 1

    logger.info(f'公式固化完成！共处理了 {len(targets)} 组选择区域（包含 {totalAreas} 个子区域）。')

def run(appComHandle, logQueue):
    utils.runWithSelection(
        appComHandle, 
        logQueue, 
        pluginInfo, 
        pickerTitle="固化公式 - 区域选取器", 
        actionFunc=_processFixValues
    )