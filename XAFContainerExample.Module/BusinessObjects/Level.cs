﻿using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace XAFContainerExample.Module.BusinessObjects {
    [DefaultClassOptions]
    public class Level : BaseObject {
        public virtual string Name { get; set; }

        public virtual string Description { get; set; }
    }
}
