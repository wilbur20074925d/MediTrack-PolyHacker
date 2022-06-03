
'use strict'

const m = require('mithril')

const Dashboard = {
  view (vnode) {
    return [
      m('.header.text-center.mb-4',
        m('h4', 'Welcome To'),
        m('h1.mb-3', 'Hospital Client'),
        m('h5',
          m('em',
            'Powered by ',
            m('strong', 'HyperLedger Sawtooth'))),
            m("img", { src: "https://cdn-icons-png.flaticon.com/512/33/33777.png"}))
     
    ]   
  }
}

module.exports = Dashboard
