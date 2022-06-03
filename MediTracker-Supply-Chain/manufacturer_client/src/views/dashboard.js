
'use strict'

const m = require('mithril')

const Dashboard = {
  view (vnode) {
    return [
      m('.header.text-center.mb-4',
        m('h4', 'Welcome To'),
        m('h1.mb-3', 'Manufacturer Client'),
        m('h5',
          m('em',
            'Powered by ',
            m('strong', 'Hyperledger Sawtooth'))),
            m("img", { src: "https://www.kindpng.com/picc/m/418-4187833_factory-clipart-manufacturing-company-manufacturing-facility-factory-icon.png"}))
     
    ]
  }
}

module.exports = Dashboard
